# merkado-socials

The working home of Merkado's social media agent (Claude). It plans, designs, drafts and reviews posts for the Merkado Facebook Page and Instagram (@merkado.cw). The Product Lead approves posts in Metricool.

Nothing in this repo touches the merkado.cw app, its database or its users. It only reads public merkado.cw pages and the merkado-cw repository.

## Start here

| File | What it is |
| --- | --- |
| [PLAYBOOK.md](PLAYBOOK.md) | How the agent works: goals, voice, rules, the weekly and daily runs, approvals. **The agent reads this first on every run.** |
| [STYLE.md](STYLE.md) | The locked visual style (Templates v1) and the Figma node of every template. |
| [CALENDAR.md](CALENDAR.md) | The launch plan and the dated calendar, week by week. |
| [LEARNINGS.md](LEARNINGS.md) | What the numbers taught us, updated every week. |
| `state/` | Logs the agent keeps: every post, product-radar watermarks, partners, takedown requests. |
| `assets/` | Rendered post images. Metricool reads them from their public GitHub URLs. |
| `captions/` | Captions, alt text and first comments per week. |

## How it runs (short version)

1. **Every Sunday afternoon** the agent reviews last week's numbers, plans next week, picks live listings, renders the posts from the locked Figma templates and puts them in Metricool as drafts.
2. **The Product Lead** opens Metricool, checks the drafts and schedules them (about 10 minutes a week).
3. **Every morning** the agent re-checks that every listing in the next 48 hours is still live and unchanged, pulls any post whose listing is gone, and looks for product updates and milestones worth announcing.

## Ownership

- Product Lead and final approver: Enrique (Kolektivo).
- Design source: Figma file `Km2x15bnTmb9R8LbnEvQTT`, page **Templates v1 · Locked (22 Oct 2026)**.
- Scheduling and analytics: Metricool brand **Merkado Curaçao** (blogId `7589417`), Facebook Page + Instagram `merkado.cw`.
