# 11 Learnings

What the numbers and the Product Lead's edits taught us. The weekly run adds a dated entry at the top. Keep each entry short: findings, one change to try, and the result of last week's change.

## 29 Oct 2026: strategy research

- Instagram names sends/shares and saves among its strongest ranking signals; Reels (and Trial Reels) are the main route to non-followers; search reads name, bio, captions and alt text. Facebook organic Page reach is low; comments, Reels and the right Page category help. Our biggest gap: no video. Experiment to propose: short Reels made from the weekly carousels.

## 28 Oct 2026: launch prep

- The Social HQ board broke once (no posts showed) because a caption with a real line break went into the page script. Fix: build the post list with json.dumps and run `node --check` plus a render test before every publish.
- Photo frames: most dealer and agency photos are 4:3 (CuraCars, Moret, Carteam's first photo), so a 936 x 700 frame shows them whole. Wide 16:9 showroom photos with a bottom-left watermark cap a frame at about 936 x 620.
- Weave free plan allows only 2 model runs from the agent in total (both used on the launch story and the first Mazda version). More AI photo extension needs a paid Weave plan. Without it: feed carousels crop only empty sides; full-photo stories need tall photos.
- Source checks: Economic Auto Center's site answers 403 to automated checks, so their cars cannot pass the pre-flight. SeriDomi shows the 2020 Honda CR-V as sold while merkado.cw still lists it as active (data issue for merkado-cw). SeriDomi also lists cars for private people (the 2019 Accent): credit SeriDomi, never the person.

- Market scan (`scripts/market_scan.py`): only 19 of 230 priced cars have 3 or more comparable live cars, so "below similar" claims will be rare and need at least 4 clean comparables. The biggest apparent bargains were data errors (a "2018" Chevrolet Spark whose slug says 2012). Car price history in merkado-cw is admin-only, so we build our own from daily public snapshots (first snapshot 28 Oct: 247 cars, 360 homes). Home price history is public on each Listing Score.
- Data issue to pass on to merkado-cw: several CuraCars mileages end in 123 (51.123, 64.123, 87.123, 92.123, 144.123 km), which looks like a placeholder or parsing artefact.

- AI photo expansion: Figma's own "Expand image" action (paid on the Figma team plan) is only in the Figma app, not reachable by the agent. Weave is linked (free plan, 150 credits). Working route: put the original photo on a padded canvas plus a mask (white = fill), upload both to Figma for a public link, run Weave "Flux Fill Pro" (4 credits per photo), then paste the original photo back on top so every original pixel stays. Each run needs the Product Lead's cost approval.

- merkado.cw returns a normal page (status 200) even for a listing that does not exist. The pre-flight must check the listing in the API (`status = active`), never only that the page loads.
- Metricool copies the image into its own storage when a draft is created (static.metricool.com). The image URL only has to work at that moment, so drafts no longer wait for a push to GitHub. The repo still keeps every JPG as the record.
- The locked T11 frame has its backdrop shade hidden; with a bright photo the white logo is unreadable. Turned it on in the copy (docs/04-design-system.md).
- Live counts 28 Oct: 247 cars, 360 real-estate listings (275 with a map location). First native listing: a 2021 Kia Picanto from a private seller.
- Data quality: Economic Auto Center has no mileage on any listing and several slugs disagree with the title (for example a 2021 Nissan Kicks whose slug says Toyota Hiace 2019); CuraCars shows impossible mileage on three older cars (1, 16 and 260 km). Skipped for now.

## 22 Oct 2026: starting point

- Instagram @merkado.cw: 13 followers, following 0. Facebook Page: 4 followers. No posting history worth measuring.
- Metricool connected 22 Oct 2026 (Facebook Page + Instagram). Brand timezone America/La_Paz (same clock as Curaçao).
- Posting times start from the October campaign research (feed 12:15 on weekdays, evening slot 18:30, Stories 19:00). Re-check with Metricool best times after 4 weeks.
- Real listing photos are mostly landscape (16:9 from Carteam Willemstad and SeriDomi, 4:3 from Economic Auto Center) and often carry dealer watermarks. Hence T11 and T12.
- Data quality notes from 22 Oct: some Economic Auto Center listings have years or slugs that disagree with their titles; two RE/MAX listings have coordinates in the sea. The pre-flight cross-checks year and price at the source.

### Hypotheses to test in the first 8 weeks
1. On Curaçao, Facebook will out-reach Instagram for listing posts; Instagram will do better for brand and map posts.
2. "The comment section" brand posts get more shares than any other series.
3. Listing posts with a clear price in the image get more saves than posts without.
4. Island Index (map) posts get the most saves.
