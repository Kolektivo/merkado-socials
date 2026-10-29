---
name: daily-check
description: Morning check for Merkado social. Re-check listings in posts due within 48 hours, pull posts whose listing is gone, flag unapproved drafts, and scan merkado-cw and merkado.cw for product news and milestones.
---

# Daily check

Keep it short and cheap when nothing needs attention. Read `AGENTS.md` first.

## Steps
0. Market snapshot: `python scripts/market_scan.py snapshot`. This builds our own dated price history from public merkado.cw data (price drops for posts, counts for milestones).
1. Pre-flight every post scheduled or drafted for the next 48 hours (playbook section 7). Pull failures back to draft and draft a replacement.
2. Drafts due in the next 36 hours that are still not approved: notify the Product Lead once per draft.
3. Radar (playbook section 9): new commits and doc changes on `Kolektivo/merkado-cw` main since `state/radar.json → last_commit`, then the watchlist in playbook section 9 checked against the live site. A watchlist item that went live: draft the posts and tell the Product Lead. Update `state/radar.json`.
4. If nothing needs attention, end quietly (one-line report, no notification).

Push changes to `state/` only when the standing approval in AGENTS.md says APPROVED.

## Report
If nothing needs the Product Lead: one line, "All clear." Otherwise start with what needs him (exact action and where to click), then pulled posts, news found and data issues, under 10 lines.
