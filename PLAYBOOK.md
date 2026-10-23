# Merkado social playbook

Status: Active, v1 (22 Oct 2026). Owner: Product Lead (Enrique). Operator: Claude (scheduled runs).
This file is the agent's operating manual. Read it fully at the start of every run, then STYLE.md, CALENDAR.md, LEARNINGS.md and the files in `state/`.

## 1. Goal

Make Merkado the first place people on Curaçao look when they want a car or a home, and the first place dealers and agencies want their stock to appear.

Launch campaign line (already on merkado.cw): **"Made to search, not scroll."** On Curaçao, finding a car or a home means scrolling Facebook groups full of "Price?", "PM" and "Still available??". Merkado is the fix: every listing in one place, with the price, the details and the seller right there.

### Targets (proposals, review after 8 weeks)

| Metric (Metricool) | Baseline 22 Oct 2026 | Target by 20 Dec 2026 |
| --- | --- | --- |
| Instagram followers | 13 | 150 |
| Facebook Page followers | 4 | 150 |
| Avg reach per feed post (IG and FB each) | none yet | 300 |
| Saves + shares per feed post (IG) | none yet | 5 |
| Clicks to merkado.cw from social (GA4, `utm_medium=social`) | none yet | Product Lead reads in GA4 |

Followers are a means. Reach to people on the island and clicks to listings are what count.

## 2. Sources of truth (in this order)

1. Live merkado.cw data and pages (what is really live today).
2. The merkado-cw repo on GitHub `Kolektivo/merkado-cw`, branch `main`: `AGENTS.md`, `docs/02-scope-and-decisions.md`, `docs/09-current-state.md`, `docs/10-execution-roadmap.md`. Read only. Never write to it.
3. This repo: PLAYBOOK.md, STYLE.md, CALENDAR.md, LEARNINGS.md, `state/`.
4. Chat summaries are never a source of truth.

If a source conflicts with this playbook (for example a feature is described in docs but not visible on merkado.cw), do not post about it. Note the conflict in the run report.

## 3. Channels and formats

| Channel | Formats | Notes |
| --- | --- | --- |
| Facebook Page `merkado.cw` | Feed image or carousel 1080×1350, Story 1080×1920 | Main stage on Curaçao (CBS Social Survey 2025: Facebook 78%, Instagram 38.5%). |
| Instagram `@merkado.cw` | Same assets, same day | Carries the look. |
| Later | Reels (launch video), TikTok, WhatsApp Channel, LinkedIn for dealers and agencies | Only after the Product Lead approves each one. |

One Metricool post covers both Facebook and Instagram (same image, same caption) unless a format needs a split.

## 4. Series (what we post)

| Series | Template(s) | What it is |
| --- | --- | --- |
| **The comment section** | T01 | The "Price? PM. Still available??" joke, answered with "Or just search." Brand posts. New comment sets for cars and for homes. |
| **On Merkado now** | T02, T03, T10, T11, T12 | Real live listings, cars and real estate, with the seller credited. Chip says **Just added** only if published on merkado.cw within the last 7 days on the post date; otherwise **For sale** or **For rent**. |
| **Island Index** | T04, T08, T09 | Monthly data from live listings: the island map with every pinned listing, neighbourhood counts, cars by type and make. Every number is dated and sourced. |
| **Before you buy** | T05 + T06 | Guide carousels built only from published Merkado Resources (merkado.cw/resources). Covers say to confirm with the official body (UOVV, a notary, a lender). |
| **List on Merkado** | T07 | For sellers: free to list, 2 listings included, WhatsApp contact. Only claims that are true on merkado.cw/pricing on the post date. |
| **What's new** | T05 + T06, T04 for milestones | Product updates and milestones (section 9). |

Mix target per 4 weeks (12 feed posts): 6 On Merkado now, 2 The comment section, 1 Island Index, 1 Before you buy, 1 List on Merkado, 1 flexible (What's new when there is news, otherwise On Merkado now). Adjust with LEARNINGS.md.

## 5. Weekly rhythm (Curaçao time, America/Curacao, UTC-4)

| Day | Time | Slot |
| --- | --- | --- |
| Monday | 12:15 | Feed: brand, guide, data or seller post (see CALENDAR.md) |
| Tuesday | 19:00 | Story: a live listing |
| Wednesday | 18:30 | Feed: real-estate listing or Island Index |
| Thursday | 19:00 | Story: a live listing (the other category from Tuesday) |
| Friday | 12:15 | Feed: car listing |

### Finding the best days and times (every weekly run)

These slots are a starting point, not fixed. Every Sunday the agent re-decides days and times from two signals:

1. **Metricool best time to post** (`getBestTimeToPostByNetwork`) for Facebook and Instagram separately, over the last 28 days: which weekdays and hours our audience is most active.
2. **Our own results**: reach, saves, shares and link clicks of every post from the last 4 to 8 weeks, grouped by weekday and time block (morning, lunch, evening) and by series, so a strong series is not mistaken for a strong day.

Rules for changing the schedule:
- Weeks 1 to 3: collect data, change nothing (too little data on a new account).
- From week 4: move a slot only when both signals point the same way, or when one slot beats the others by at least 30% on average reach over 3 or more posts.
- Change one thing per week (one day or one time), so the effect can be measured. Keep 3 feed posts and 2 Stories a week unless LEARNINGS.md shows more helps.
- Facebook and Instagram may get different times. If they differ by more than 2 hours, schedule the network posts separately.
- Monthly: test one new slot (for example Saturday morning or Sunday evening) with a listing post and compare.
- Write every change and its result in LEARNINGS.md, and update the table above and CALENDAR.md.

## 6. Voice and captions

- English only for now (Product Lead, 10 Oct 2026). Papiamentu and Dutch later.
- Short, warm, plain, local. Talk like a helpful neighbour who knows the market, not like an ad.
- Lead with the useful thing (price, place, what it is). No hype words ("amazing", "dream", "don't miss out"), no em dashes, no ALL CAPS, at most one emoji and only if it adds meaning.
- Never invent facts, numbers, quotes, testimonials or partners. Every number comes from live data with a date.
- 3 to 5 hashtags, at the end: always `#Curaçao`, plus the fitting ones from `#Willemstad #CuraçaoCars #CuraçaoRealEstate #CarsForSale #HomesForSale #ForRent`.
- Links: no URL in the caption. Put the full link with UTM in the first comment: `https://merkado.cw/<path>?utm_source=social&utm_medium=metricool&utm_campaign=<series-slug>&utm_content=<post-id>`. The caption ends with "Link in the first comment" on listing posts, or "Search it on merkado.cw" on brand posts.
- Alt text on every image: one plain sentence describing what is shown.

### Caption skeletons

Listing (car):
```
<Year> <Make> <Model>, <mileage> km, <fuel>, <gearbox>.
XCG <price>, listed by <Seller>.
<One useful line: what it suits, from the listing itself, never invented.>

Details come from <Seller>'s listing. Always check the original listing and contact the seller for official details.
(If the photo was AI-expanded:) Background extended with AI; the car is shown as photographed.
Link in the first comment.
#Curaçao #CuraçaoCars #CarsForSale
```

Listing (real estate): same, with type, bedrooms, bathrooms, m², neighbourhood, sale or rent.

Brand / data / guide: a hook line, two or three short lines of substance, a plain call to action.

## 7. Listing posts: picking, checking, crediting

### Picking
- Only `status = active` listings that merkado.cw shows publicly, with a real price (no "Price on request"), at least one sharp photo that shows the car or property itself, and complete key fields (cars: make, model, year, price; mileage optional but preferred. Real estate: type, price, neighbourhood; bedrooms for homes).
- Prefer variety: different sellers, price ranges and neighbourhoods across a week. Never the same listing twice in 30 days. Never more than one listing from the same seller per week unless they opted in as a partner.
- Prefer native Merkado listings (`listing_origin = native`) when their owner has agreed to promotion. Until the Terms and an opt-in exist, native listings are posted only with the owner's written yes (log it in `state/partners.csv`).
- Skip photos with a recognisable private person, a screenshot, a collage, heavy text banners that cover the car, or another platform's interface.

### Pre-flight check (when drafting AND again within 48 hours of publishing)
1. The listing is still returned by the merkado.cw API with `status = active`.
2. The original listing (source page) still loads and still shows the listing: not 404 or 410, not redirected to a homepage, not marked sold, reserved or rented. For cars, read the source link from the merkado.cw car page.
3. Price, year and mileage (cars) or price, type and bedrooms (real estate) match between merkado.cw, the source page and the post. If merkado.cw and the source disagree, skip the listing and note it in the run report as a data issue.
4. The photo still loads.
5. Any failure: do not publish. Turn the post back into a draft (`updateScheduledPost` with `draft: true`), log the reason in `state/posts.csv`, and propose a replacement draft.

### Credit and disclaimer
- Every scraped listing shows the seller in the post ("Via <Seller>" on the card) and in the caption ("listed by <Seller>").
- Caption disclaimer on every listing post: "Details come from <Seller>'s listing. Always check the original listing and contact the seller for official details."
- Tag the seller's own Instagram or Facebook account only when it is confirmed in `state/partners.csv`. Never guess a handle.
- Team decision (Oct 2026): we use dealer and agency photos with credit; if a seller asks us to remove a post, remove it within 24 hours and log it in `state/takedowns.md`. Do not post that seller again unless they opt in.

### Privacy and naming
- Never show a private seller's name, phone number or face. Business names are fine.
- **Featured** is reserved for paid Sentoo placements. Organic picks are never called Featured.
- Listing Score is described as listing completeness, never property quality or a valuation.

## 8. Data posts (Island Index)

- Numbers come from the live merkado.cw API on the render date, and the post prints that date and "on merkado.cw".
- The island map (T08) is drawn from OpenStreetMap data via CARTO vector tiles and must print "Map data © OpenStreetMap · © CARTO". Leave out pins that fall in the sea and report them as data issues.
- Counts are "listings" unless the filter really is homes only.

## 9. Product updates and milestones (the radar)

The daily run reads the merkado-cw repo and live merkado.cw to find news worth posting.

### What to watch
- New commits on `main` of `Kolektivo/merkado-cw` since `state/radar.json → last_commit`.
- Changes to `docs/09-current-state.md`, `docs/10-execution-roadmap.md`, `docs/02-scope-and-decisions.md`.
- Live counts (cars, real estate, native listings, businesses) once per day.

### What counts as news
- A user-facing feature that is **visible on merkado.cw today** (check the page). Code on `main` that is not deployed, behind a flag, private beta or allowlisted is not news yet.
- A milestone crossing a threshold in `state/radar.json → milestones` (for example 300 cars, 500 listings, first business account live, first Featured car).
- Payments go-live: when Featured and the extra listing can be bought by every seller (allowlist removed). This starts the payments launch arc in CALENDAR.md.

### What is never news
- Property Match while it is a private beta. Paid features that are not switched on. Merkado Rent Advance or anything from merkado-labs. Internal ops, scrapers, security, refactors, SEO plumbing. Anything only described in docs/private.

### What to do with news
1. Write a one-paragraph brief in the run report: what changed, who it helps, proof it is live (URL).
2. Draft the post(s) as Metricool drafts: T05 cover + T06 slides for a feature, T04 for a milestone, plus a Story. Put them in the next free feed slot or, for big news, the next day at 12:15.
3. Push-notify the Product Lead: "News found: <title>. Drafts ready for your approval."

## 10. Production pipeline (how a post is made)

### Data
- Cars: `GET https://merkado.cw/api/cars?sort=newest&page=<n>` (24 per page; fields include id, slug, make, model, trim, year, price, mileage, fuel_type, transmission, body_type, status, published_at, source_name, listing_origin, primary_image_url). Count: `/api/cars/count`. Car page: `https://merkado.cw/car/<slug>` (has the "original listing" link for scraped cars).
- Real estate: `GET https://merkado.cw/api/real-estate/map` (all active listings with latitude, longitude, price_xcg, listing_type sale or rent, real_estate_type, bedrooms, bathrooms, neighbourhood, source_name, source_url, primary_image_url, slug). Page: `https://merkado.cw/real-estate/<slug>`.
- Photos: always through merkado.cw, never hot-linked: `https://merkado.cw/_next/image?url=<url-encoded primary_image_url>&w=1920&q=90`.
- Source pages: WebFetch the source URL to confirm it is live and to read price and year.
- Network access order: (1) the workspace shell (`curl`) if merkado.cw is reachable; (2) the linked computer's built-in browser (`mcp__remote-devices__Claude_Browser__*`, fetch from a merkado.cw tab) if those tools are present; (3) otherwise stop, and notify the Product Lead that merkado.cw is not reachable from the cloud workspace (fix: Settings → Capabilities → allowed domains: `merkado.cw`, `figma.com`, `*.figma.com`).

### Design (Figma)
1. `create_session` on file `Km2x15bnTmb9R8LbnEvQTT`, then load the figma-use skill before any `use_figma` call.
2. Duplicate the template frame from page **Templates v1 · Locked (22 Oct 2026)** (node IDs in STYLE.md) onto the page **Posts · <ISO week>** (create it if missing). Name the frame `<date> · <series> · <slug>`.
3. Replace only the content (texts, photo, chip label). Never move, restyle or recolour template parts. Follow the photo rules in STYLE.md (AI expansion with its guardrails, or the blurred backdrop).
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
- If the account supports the review flow, use `createScheduledPostForReview` with reviewer `enrique@kolektivo.co` and `approvalSystem: "any"` instead of a draft. If it errors once, fall back to drafts and note it in LEARNINGS.md.
- Log every post in `state/posts.csv`.

## 11. Approvals: what the agent may and may not do

May, without asking:
- Read merkado.cw, the merkado-cw repo (read only), Metricool analytics.
- Create and edit Figma frames in the posts pages of the design file.
- Commit and push to `main` of this repo (assets, captions, state, LEARNINGS.md, CALENDAR.md updates). Standing approval: see the line at the end of this file.
- Create Metricool **drafts** (or posts sent for review), and turn a scheduled post back into a draft when its pre-flight fails.

Must not:
- Publish or schedule a post to go live without the Product Lead's approval. The Product Lead approves by scheduling the draft in Metricool (or approving it in the review flow).
- Delete published posts, reply to comments or DMs, follow or unfollow accounts, post in Facebook groups, run ads or boosts, or spend money.
- Change the templates on the locked page, the brand colours or fonts.
- Write to the merkado-cw repo, Supabase, Vercel or any merkado.cw system.
- Contact dealers, agencies or anyone else.

## 12. The weekly run (Sunday)

1. Read this playbook, STYLE.md, CALENDAR.md, LEARNINGS.md, `state/`. Check whether Figma Weave is linked (`weave_find_model` with query "expand image"); if it is, use AI-expanded listing photos (STYLE.md, version A), otherwise the blurred backdrop (version B).
2. Analytics for the last 7 days and the last 28 days (Metricool): reach, interactions, saves, shares, followers gained per network, per post, plus best time to post per network. Re-decide days and times with section 5 "Finding the best days and times". Write 3 to 5 findings and 1 change to try next week in LEARNINGS.md.
3. Check last week's drafts: which were approved, edited or left. Learn from edits (compare the published caption to the draft).
4. Plan next week from CALENDAR.md, adjusted by the findings. If it is the first full week of a month, include Island Index.
5. Pick listings (section 7), run the pre-flight, render, export, push, create drafts.
6. Captions file `captions/<YYYY>-W<ww>.md`.
7. Update CALENDAR.md (what was planned, what is drafted) and `state/posts.csv`. Commit and push.
8. Update the Social HQ page (artifact `https://claude.ai/artifact/TkELSi7UsrQCugHZ88b6im`): read it first with the Artifact tool (`action: read`), replace only the part between `<!-- THIS-WEEK:START` and `<!-- THIS-WEEK:END -->` with this week's drafts (thumbnails published as files under `week/`, date, slot, title, status) and last week's top numbers, then publish to the same url. Leave the rest of the page as it is.
9. Report (section 14) and push-notify: "Week <ww> is ready: <n> drafts waiting in Metricool."

## 13. The daily run (morning)

1. Pre-flight every post scheduled or drafted for the next 48 hours (section 7). Pull failures back to draft and draft a replacement.
2. Drafts due in the next 36 hours that are still not approved: notify the Product Lead once per draft.
3. Radar (section 9). Update `state/radar.json`.
4. If nothing needs attention, end quietly (one-line report, no notification).

## 14. Run report format

Start with one line: what happened. Then, only if relevant: Drafts created (date, slot, title, Metricool link), Pulled posts (why), News found, Data issues (listing id, what disagrees), Needs you (exact action, where to click). Keep it under 15 lines.

## 15. When something fails

- Never post a guess. Skip, log, report.
- If a tool fails twice, stop that step and report it; do not loop.
- If Figma or Metricool limits are hit, report and finish the rest.

## 16. Takedowns and complaints

Any request to remove a post or stop using someone's photos: the Product Lead forwards it, or it arrives in the run's context. Remove from Metricool if still scheduled; if already published, ask the Product Lead to delete it (the agent cannot delete published posts). Log in `state/takedowns.md`. Add the seller to the do-not-post list in `state/partners.csv`.

---

Standing approval: PENDING. The Product Lead has not yet approved autonomous pushes to this repo. Until this line says APPROVED with a date, scheduled runs must not push; they render, write locally, and report.
