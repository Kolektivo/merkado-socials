# 12 Setup (for the Product Lead)

One-time setup, then a weekly 10-minute habit. Windows 11 + PowerShell.

## One time

1. **Approve the first push.** Reply "Approved, commit and push" in the Claude chat that built this repo. Result: the repo appears on GitHub with these files.
2. **Allow the domains.** On claude.ai in a web browser: Settings → Capabilities → allowed domains. Add `merkado.cw`, `figma.com`, `mcp.figma.com`. (Team plan: your admin does it under Organization settings → Capabilities.) Result: the Sunday run can read listings and use Figma.
3. **Link Figma to Weave.** Open https://app.weavy.ai/settings?section=profile, sign in, link your Figma account. Result: AI photo expansion works.
4. **Paste the profile texts** from `captions/profile.md` into Instagram (Edit profile) and the Facebook Page (Edit details).
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

- **Sunday evening:** you get a push and an email "Week N is ready". Open Metricool → Planner, check the drafts, press Schedule on the ones you like. Edit captions freely; the agent learns from your edits.
- **Mornings:** a push only if something needs you (a listing sold, a draft not approved, news found).

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
