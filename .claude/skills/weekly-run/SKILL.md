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
1. Read AGENTS.md, docs/03-content-playbook.md, docs/04-design-system.md, docs/10-calendar.md, docs/11-learnings.md, `state/`. Check whether Figma Weave is linked (`weave_find_model` with query "expand image"); if it is, use AI-expanded listing photos (docs/04-design-system.md, version A), otherwise the blurred backdrop (version B).
2. Analytics for the last 7 days and the last 28 days (Metricool): reach, interactions, saves, shares, followers gained per network, per post, plus best time to post per network. Re-decide days and times with playbook section 5 "Finding the best days and times". Write 3 to 5 findings and 1 change to try next week in docs/11-learnings.md.
3. Check last week's drafts: which were approved, edited or left. Learn from edits (compare the published caption to the draft).
4. Plan next week from docs/10-calendar.md, adjusted by the findings. If it is the first full week of a month, include Island Index.
5. Pick listings (playbook section 7), run the pre-flight, render, export, push, create drafts.
6. Captions file `captions/<YYYY>-W<ww>.md`.
7. Update docs/10-calendar.md (what was planned, what is drafted) and `state/posts.csv`. Commit and push.
8. Update the Social HQ page (artifact `https://claude.ai/artifact/TkELSi7UsrQCugHZ88b6im`): read it first with the Artifact tool (`action: read`), replace only the part between `<!-- THIS-WEEK:START` and `<!-- THIS-WEEK:END -->` with this week's drafts (thumbnails published as files under `week/`, date, slot, title, status) and last week's top numbers, then publish to the same url. Leave the rest of the page as it is.
9. Report (playbook section 14) and push-notify: "Week <ww> is ready: <n> drafts waiting in Metricool."

For each post, follow `.claude/skills/make-post/SKILL.md`.
