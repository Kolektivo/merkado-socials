# 05 Architecture and integrations

How the agent is built and how a post is made. Values that change per project live in `config/brand.json`.

## The parts

| Part | What it does | Where |
| --- | --- | --- |
| This repo | The agent's memory: rules, style, calendar, learnings, logs, rendered images | GitHub `Kolektivo/merkado-socials` (public, so Metricool can read image URLs) |
| Skills | Step-by-step procedures any Claude session can run | `.claude/skills/` (weekly-run, daily-check, make-post) |
| Cloud routines | Start a fresh Claude cloud session on a timer that runs a skill | claude.ai/code/routines: "Merkado social weekly run" (Sun 16:37 Curaçao, Opus, `trig_01HeGprXitgepcTdbMh6SJAj`), "Merkado social daily check" (daily 07:36, Sonnet, `trig_01MmHKSctQ3PKpsYHdy9iAUT`). Connectors: Figma and Metricool only (no mail or chat tools, so a run cannot message anyone outside the Claude app) |
| Figma | Locked templates and every rendered post | File `Km2x15bnTmb9R8LbnEvQTT` |
| Figma Weave | AI photo expansion (outpainting) | Needs the Product Lead's Figma account linked to Weave |
| Metricool | Drafts, approval, publishing, analytics, best times | Brand "Merkado Curaçao", blogId `7589417` |
| merkado.cw | Live listing data and photos (read only) | Public API and pages |
| merkado-cw repo | Product updates for the radar (read only) | GitHub `Kolektivo/merkado-cw` |
| Social HQ page | Visual summary for the Product Lead, "this week" refreshed by the weekly run | claude.ai artifact `TkELSi7UsrQCugHZ88b6im` |

Interactive work (new templates, campaigns, fixes) happens in Claude Code or Cursor on a local clone of this repo. Claude Code logged in with the Product Lead's claude.ai account gets the Figma and Metricool connectors automatically.

## Network access for cloud runs

Cloud runs (Claude Code routines) can only reach the domains their cloud environment allows. The Figma and Metricool connectors do not need an entry: connector traffic goes through Anthropic, not the session's network. GitHub is allowed by default.

Set it on claude.ai/code: environment selector (first control under the message box) → Cloud → hover the **Default** environment → settings icon → **Network access** → **Custom**, tick **Also include default domains**, and list one per line:

```
merkado.cw
figma.com
*.figma.com
autobedrijfwillemstad.com
*.autobedrijfwillemstad.com
curacars.com
*.curacars.com
seridomi.com
economic.cw
*.economic.cw
realestate-curacao.com
*.realestate-curacao.com
kw-curacao.com
moretrealestate.com
monumentenzorg.cw
```

Figma's domains are needed because photo uploads and image exports go from the shell. The seller sites are needed for the pre-flight check at the source. Add a domain here when a new seller source appears. Note: claude.ai Settings → Capabilities → "Allow network egress" is a different setting (for claude.ai chats), not used by the cloud runs.

## How a post is made

### Data
- Cars: `GET https://merkado.cw/api/cars?sort=newest&page=<n>` (24 per page; fields include id, slug, make, model, trim, year, price, mileage, fuel_type, transmission, body_type, status, published_at, source_name, listing_origin, primary_image_url). Count: `/api/cars/count`. Car page: `https://merkado.cw/car/<slug>` (has the "original listing" link for scraped cars).
- Real estate: `GET https://merkado.cw/api/real-estate/map` (all active listings with latitude, longitude, price_xcg, listing_type sale or rent, real_estate_type, bedrooms, bathrooms, neighbourhood, source_name, source_url, primary_image_url, slug). Page: `https://merkado.cw/real-estate/<slug>`.
- Photos: always through merkado.cw, never hot-linked: `https://merkado.cw/_next/image?url=<url-encoded primary_image_url>&w=1920&q=90`.
- Source pages: WebFetch the source URL to confirm it is live and to read price and year.
- Network access order: (1) the workspace shell (`curl`) if merkado.cw is reachable; (2) the linked computer's built-in browser (`mcp__remote-devices__Claude_Browser__*`, fetch from a merkado.cw tab) if those tools are present; (3) otherwise stop, and notify the Product Lead that merkado.cw is not reachable from the cloud workspace (fix: on claude.ai in a web browser, Settings → Capabilities → allowed domains: `merkado.cw`, `figma.com`, `mcp.figma.com`).

### Design (Figma)
1. `create_session` on file `Km2x15bnTmb9R8LbnEvQTT`, then load the figma-use skill before any `use_figma` call.
2. Duplicate the template frame from page **Templates v2 · 29 Oct 2026** (`88:182`, node IDs in `state/templates.json`) onto the page **Posts · <ISO week> (<dates>)** (create it if missing). Name the frame `<date> · <series> · <slug>`.
3. Replace only the content (texts, photo, chip label). Never move, restyle or recolour template parts. Follow the photo rules in docs/04-design-system.md (AI expansion with its guardrails, or the blurred backdrop).
4. Photos: `upload_assets` with `nodeIds` set to the photo rectangle(s), then POST the image bytes to each submit URL (from the shell, or from the browser tab when the shell cannot reach figma.com).
5. Check the result with `get_screenshot`: no text overflow past the 72 px margins, no clipped words, photo shows the subject.

### Export and hosting
1. `get_screenshot` with `enableBase64Response: true` and `maxDimension` 1350 (feed) or 1920 (story). The tool saves a full-size PNG; convert it to JPG (quality 90) with Python PIL.
2. Save as `assets/<YYYY>-W<ww>/<YYYY-MM-DD>_<slot>_<slug>.jpg`. Commit and push to `main` of this repo.
3. Public URL: `https://raw.githubusercontent.com/Kolektivo/merkado-socials/main/assets/...`. Check it returns 200 before using it.

### Metricool
- Brand: blogId `7589417`, timezone `America/La_Paz` (same clock as Curaçao).
- Feed post: `createScheduledPost` with `draft: true`, providers facebook + instagram, `instagramData.type = POST`, `facebookData.type = POST`, `isAiGenerated` true only when the image contains AI imagery, `mediaAltText`, `firstCommentText` with the UTM link.
- Story: same, with `type = STORY` on both networks and no text.
- If the account supports the review flow, use `createScheduledPostForReview` with reviewer `enrique@kolektivo.co` and `approvalSystem: "any"` instead of a draft. If it errors once, fall back to drafts and note it in docs/11-learnings.md.
- Log every post in `state/posts.csv`.


## Routine prompts

Kept here so they can be recreated exactly. Both routines use the Default cloud environment, check out both repos, and are scheduled in UTC (weekly `37 20 * * 0`, daily `36 11 * * *`; Curaçao is UTC-4 all year).

- Weekly run: "Get Kolektivo/merkado-socials (push) and Kolektivo/merkado-cw (read). Read AGENTS.md and follow `.claude/skills/weekly-run/SKILL.md`."
- Daily check: "Get Kolektivo/merkado-socials (push) and Kolektivo/merkado-cw (read). Read AGENTS.md and follow `.claude/skills/daily-check/SKILL.md`."

The full prompt text also repeats the safety rules from AGENTS.md, so a run stays safe even if the repo cannot be read.
