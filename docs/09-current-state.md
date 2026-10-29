# 09 Current state

Last updated: 28 Oct 2026.

## Working
- Repo set up in Claude Code on the Product Lead's PC (28 Oct). From there Figma, Metricool and merkado.cw all work.
- Figma file cleaned up on 29 Oct: Templates v2 (page 88:182, 14 templates), Posts · 2026-W44 (88:183), Posts · 2026-W45 (88:184), Posts · upcoming drafts (88:185), One-off library (88:186), Brand assets (10:18), Product Lead · iterations (88:187). Old rounds deleted; restorable from version history.
- Social strategy written (docs/01) and on the Social HQ page, with Templates v2, the One-off library and the reply kit (captions/reply-kit.md).
- Metricool connected: Facebook Page "Merkado Curaçao" and Instagram merkado.cw. Baseline 22 Oct: Instagram 13 followers, Facebook 4. No posts yet on either.
- Launch Thu 29 Oct 2026. Scheduled in Metricool after the Product Lead's approval in chat (28 Oct): launch post Thu 12:15, car carousel Fri 30 Oct 12:15 (city cars under XCG 20.000), real estate carousel Wed 4 Nov 18:30 (rentals under XCG 3.000). The Thu 19:00 story (Kia Sorento, style C) is scheduled too (approved 29 Oct). Story styles B and C chosen 29 Oct (Figma page `Round 10 · Story options (28 Oct)`). The carousel look (Round 9) is approved. Feed alternates paper and violet for the grid (29 Oct).
- Profiles are live as the Product Lead set them (name, short bio, link to merkado.cw). Good enough for launch; optional tweak in `captions/profile.md`.
- Private (native) listings may be posted without a written yes (28 Oct).
- Social HQ page for the Product Lead, now with the weekly approval board (launch week filled in, 28 Oct).
- Approval works in chat: the Product Lead replies, the agent schedules in Metricool (28 Oct).
- Market scan (`scripts/market_scan.py`): first price snapshot 28 Oct (247 cars, 360 homes); ranked picks with reasons. Price drops become visible once daily snapshots run.
- News radar: merkado-cw main unchanged since 22 Oct (e9b246c). Business pages are live (Weber & Weber), but its page showed no listings on 29 Oct, so the What's new post waits. Payments still limited to the Product Lead; Property Match still private beta.

## Blocked or waiting
- Automatic runs: two cloud routines created 29 Oct 2026, connectors Figma and Metricool only. Weekly run Sundays 16:37 (first run Sun 1 Nov), daily check 07:36 (first run Fri 30 Oct). Not yet tested by a real run.
- Standing approval for scheduled runs to push: APPROVED 29 Oct 2026 (AGENTS.md).
- Figma Weave linked 28 Oct, but the free plan allows only 2 runs from the agent (both used). AI photo extension is switched off (not scalable).
- Cloud environment network access: set by the Product Lead on 28 Oct (Custom list from docs/05). First tested by the daily check on 30 Oct.
- Metricool review flow (approve by email) not tested; drafts are the default.

## Known data issues (merkado.cw)
- merkado.cw returns a normal page for listings that do not exist; the pre-flight checks the API instead (28 Oct).
- Economic Auto Center: no mileage on any listing, several slugs disagree with titles (28 Oct). CuraCars: three older cars with impossible mileage (28 Oct).
- Two RE/MAX listings with coordinates in the sea (Harmonie, Blue Bay), 22 Oct.
