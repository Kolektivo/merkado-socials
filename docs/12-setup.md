# 12 Setup (for the Product Lead)

One-time setup, then a weekly 10-minute habit. Windows 11 + PowerShell.

## One time

1. **Approve the first push.** Reply "Approved, commit and push" in the Claude chat that built this repo. Result: the repo appears on GitHub with these files.
2. **Allow the domains for the cloud runs.** On claude.ai/code, open the Default cloud environment's settings and set Network access to Custom with the domain list in `docs/05-architecture-and-integrations.md` ("Network access for cloud runs"). Result: the Sunday run can read listings, check seller sites and use Figma.
3. **Weave:** linked on 28 Oct; no longer needed (AI photo extension is switched off).
4. **Profile set-up (10 minutes).** Instagram: pin the launch post now (open the post, tap the three dots, Pin to your profile), and pin List on Merkado and the Island map once they are live. Add story Highlights Cars, Homes, Bargains, Guides, Sell (Claude makes the covers). Optional: the bio and tracked link from `captions/profile.md`. Facebook: your Page, Settings, Page setup, Category: set Internet company first and keep Real estate second.
5. **Install Git for Windows** if you don't have it: https://git-scm.com/downloads/win (all default options).
6. **Install Claude Code** (skip if `claude --version` already prints a version). In PowerShell:
   ```powershell
   irm https://claude.ai/install.ps1 | iex
   ```
   Close PowerShell, open a new one, run `claude --version`. Expected: a version number.
7. **Get the repo on your PC.** In PowerShell:
   ```powershell
   cd $HOME\Documents
   git clone https://github.com/Kolektivo/merkado-socials.git
   cd merkado-socials
   claude
   ```
   Log in with the same claude.ai account when the browser opens.
8. **Check the connectors.** In Claude Code type `/mcp`. Expected: Figma and Metricool in the list (they come from your claude.ai account). If missing, type `/status` and check you are logged in with your claude.ai subscription, not an API key.
9. **First prompt** (paste into Claude Code):
   ```
   Read AGENTS.md and docs/00-docs-index.md. Check that you can reach Figma (file Km2x15bnTmb9R8LbnEvQTT), Metricool (blogId 7589417) and merkado.cw. Then give me a 5-line status: what works, what is blocked, and what I need to do. Do not change anything yet.
   ```

## Every week

- **Sunday evening:** a new session "Merkado social weekly run" appears in the Claude app (claude.ai/code) with "Week N is ready" and the Social HQ link. Look at the posts, then reply in that session: "Approve all", "Approve 1 and 3", "Change 2: ..." or "Skip 4". The agent schedules what you approved.
- **Mornings:** the daily check runs at 07:36. Open it only if it says something needs you (a listing sold, news found, a comment to answer).
- **Manage the runs:** claude.ai/code/routines. Open a routine to pause it, change its time, or press Run now.

## Handy prompts in Claude Code

| You want | Type |
| --- | --- |
| Prepare the week now (instead of waiting for Sunday) | `/weekly-run` |
| Check upcoming posts and news now | `/daily-check` |
| One extra post | `/make-post a Story for the newest home for rent in Jan Thiel` |
| A new idea or campaign | `Read AGENTS.md. Plan a <idea> campaign for 2 weeks using the locked templates. Plan only, no drafts yet.` |
| A new template | `Read AGENTS.md and docs/04-design-system.md. Design 3 options for a <type> post in Figma on a new page. Do not touch the locked page.` |

## Reuse for another project

On GitHub, open this repo → Settings → tick "Template repository". For a new project: "Use this template", then ask Claude Code: `Read AGENTS.md and README.md. Adapt this repo to <project>: rewrite config/brand.json, docs 01 to 04 and the calendar, keep the skills. Ask me what you need to know first.`
