---
name: weekly-run
description: Plan, design and draft next week's Merkado social posts in Metricool, review last week's numbers and adjust days, times and mix. Use on Sundays or when asked to prepare the week.
---

# Weekly run

Prepares Monday to Sunday of next week. Read `AGENTS.md` first; its hard rules apply to every step.

## Before you start
- Get the repos: this repo (push) and `Kolektivo/merkado-cw` (read only).
- If merkado.cw or figma.com is not reachable, follow docs/05-architecture-and-integrations.md "Network access". If neither route works, stop the listing work and report the fix.
- Push only when the standing approval in AGENTS.md says APPROVED.

## Steps
1. Read AGENTS.md, docs/03-content-playbook.md, docs/04-design-system.md, docs/10-calendar.md, docs/11-learnings.md, `state/`.
2. Analytics for the last 7 days and the last 28 days (Metricool): reach, interactions, saves, shares, followers gained per network, per post, plus best time to post per network. Re-decide days and times with playbook section 5 "Finding the best days and times". Write 3 to 5 findings and 1 change to try next week in docs/11-learnings.md.
3. Check last week's drafts: which were approved, edited or left. Learn from edits (compare the published caption to the draft).
4. Plan next week from docs/10-calendar.md, adjusted by the findings. If it is the first full week of a month, include Island Index. Follow playbook section 4 "Earning money, the natural way" (seller lines, direct-listing stories, the monthly Sell story, paid features as news once live).
5. Pick listings with `python scripts/market_scan.py picks car` and `picks home` (playbook section 7 "Strategy"): every pick gets one angle that shows in the post. For feed posts use `python scripts/market_scan.py roundup car <theme>`: a round-up carousel with one listing per seller (mix in homes when fewer than 3 car sellers qualify), bargain themes first. Look at every photo and skip heavy banners and screenshots (playbook section 7). Then run the pre-flight, render, export, push, create drafts. In the approval message, give each listing its one-line reason.
6. Captions file `captions/<YYYY>-W<ww>.md`.
7. Update docs/10-calendar.md (what was planned, what is drafted) and `state/posts.csv`. Commit and push.
8. Update the Social HQ page (artifact `https://claude.ai/artifact/TkELSi7UsrQCugHZ88b6im`): read it first with the Artifact tool (`action: read`), replace only the part between `<!-- THIS-WEEK:START` and `<!-- THIS-WEEK:END -->` (the approval board: the `WEEK` list in the script plus the heading and lede) with this week's posts (images published as files under `week/`, number, day and time, network, caption, checks done) and last week's top numbers, build the `WEEK` list with json.dumps (never hand-typed strings), check the page script with `node --check` and a render test, then publish to the same url. Leave the rest of the page as it is.
9. Send the approval message (AGENTS.md "Approval message") and push-notify: "Week <ww> is ready: <n> posts waiting for your OK."
10. When the Product Lead replies: schedule exactly the approved posts (`updateScheduledPost` with `draft: false`, everything else unchanged), make any changes he asked for first and show them again, leave skipped posts as drafts, then confirm each post's time. Log statuses in `state/posts.csv` and `docs/10-calendar.md`.
11. First Sunday of the month: add the monthly report (playbook section 14) to the message.


For each post, follow `.claude/skills/make-post/SKILL.md`.
