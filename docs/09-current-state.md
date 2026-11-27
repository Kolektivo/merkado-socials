# 09 Current state

Last updated: 27 Nov 2026.

## Working
- Live on Facebook (Page "Merkado Curaçao") and Instagram (@merkado.cw) since Thu 29 Oct 2026. Weeks 44 to 47 are published; week 48 (23 to 29 Nov) was approved in chat on 22 Nov and scheduled unchanged. Per-post status: `docs/10-calendar.md` and `state/posts.csv`.
- Cloud routines run on their own (checked 27 Nov): "Merkado social weekly run" (Sundays 16:37 Curaçao, Opus) and "Merkado social daily check" (daily 07:36, Sonnet), both enabled, both on the Merkado cloud environment, connectors Figma and Metricool. Every daily check since 15 Nov ran and succeeded; the weekly runs of 15 and 22 Nov drafted, captioned and, after approval, scheduled their weeks. Details: docs/05-architecture-and-integrations.md.
- Approval works in chat: the weekly run sends "Week N is ready", the Product Lead replies, the run schedules exactly the approved posts.
- Market scan (`scripts/market_scan.py`): a daily price snapshot since 28 Oct builds our own price history; verified price drops now feed posts (the Fri 27 Nov price-drop carousel).
- Figma: Templates v2 (88:182) locked; a posts page per week (W46 110:304, W47 122:245, W48 136:148).
- Social HQ page with the weekly approval board, updated by each weekly run.
- Repo works from its new folder on the Product Lead's PC (moved 26 Nov; checked 27 Nov: skills present, market scan runs, local main matches GitHub).
- Payments are open to every seller on merkado.cw since 30 Oct (Featured XCG 50 for 7 days, extra listing XCG 15); the daily check looks for Featured listings every morning (none on 24 to 27 Nov).

## Blocked or waiting
- Saving from cloud runs: on 24 and 27 Nov the cloud's safety check refused the run's combined edit-and-push command. The 24 Nov snapshot never reached GitHub, and the 27 Nov pre-flight notes were not logged (the pre-flight itself passed). The save steps in the project rules ("Git" section) were split on 27 Nov so each step runs on its own; not yet proven by a cloud run.
- Growth is flat: Instagram 16 followers (22 Nov, from 13 on 22 Oct), reach 5 to 8 per post, no saves or shares since launch week. The 8-week review on 20 Dec weighs Reels made from the carousels.
- Instagram stories can fail on their own: the Tue 17 Nov story published on Facebook only ("media cannot be found" on Instagram). Proposed in docs/11-learnings.md (22 Nov): the daily check looks at each story's status after 19:00. Not yet part of the daily check.
- Seller sites the cloud run cannot always read: economic.cw (403 at times; answered again on 22 Nov), realestatecaribe.com (refused on 24 Nov). Those listings are then pre-flighted on merkado.cw only.
- merkado.cw returned 402 once (21 Nov morning); that day's snapshot was skipped and the site was back the same day.
- Milestones reached but not posted yet (state/radar.json): 250 active cars (30 Oct), 400 and 500 real estate listings (by 8 Nov).
- Figma Weave: free plan used up; AI photo extension is switched off.
- Metricool review flow (approve by email) not tested; drafts are the default.

## Known data issues (merkado.cw)
- merkado.cw returns a normal page for listings that do not exist; the pre-flight checks the API instead (28 Oct).
- Economic Auto Center: no mileage on any listing, several slugs disagree with titles (28 Oct). CuraCars: three older cars with impossible mileage (28 Oct).
- Two RE/MAX listings with coordinates in the sea (Harmonie, Blue Bay), 22 Oct.
- Joubert Realty rentals show about 1.6% more on merkado.cw than on Joubert's own pages (22 Nov). The first native property (Vista Royal land) has a map screenshot as its first photo (22 Nov).
