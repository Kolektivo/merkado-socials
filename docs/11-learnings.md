# 11 Learnings

What the numbers and the Product Lead's edits taught us. The weekly run adds a dated entry at the top. Keep each entry short: findings, one change to try, and the result of last week's change.

## 8 Nov 2026: weekly run, week 45 numbers

Numbers (Metricool, posts 2 to 8 Nov):
- Island Index neighbourhoods (Mon 12:15): Instagram reach 8, 31 views, 3 likes; Facebook reach 9, 12 impressions, 2 reactions. Best Facebook reach so far.
- Rentals under XCG 3.000 carousel (Wed 18:30): Instagram reach 7, 29 views; Facebook reach 3, 2 clicks.
- SUVs carousel (Fri 12:15): Instagram reach 5, 15 views; Facebook reach 3, 3 clicks.
- Stories (Tue 3 Nov Kia Optima): Metricool reports reach 0 and 3 exits, so story reach is not usable yet.
- Instagram followers 15 (14 on 1 Nov). No saves, shares or comments on any week 45 post.
- 28 days so far: the launch brand post is still the best post by far (Instagram reach 31). Listing carousels sit at 5 to 9.

Findings:
1. Week 2 of 3 of the "collect, change nothing" rule: days and times stay. Metricool still has no Instagram best-time data; Facebook again peaks 10:00 to 12:00 on weekdays (Wednesday strongest), which supports 12:15 and puts the Wed 18:30 slot in a weaker hour (watch it next week, change in week 4 only if the rule allows).
2. Data and brand posts out-reach listing carousels on both networks (Island Index FB 9 vs carousels 3). Facebook clicks come from the carousels (2 and 3), so carousels drive visits even with low reach.
3. Reach is falling post by post on Instagram (31, 9, 8, 7, 5). With 15 followers almost all reach is followers; the account needs content that travels (shares) or Reels to reach new people.
4. Supply, not ideas, limits the week: from the cloud run only RE/MAX, Moret and Keller Williams (homes) and Carteam and CuraCars (cars) can be pre-flighted. Six new agencies (At Home 119, Sunset 57, Real Estate Caribe 25, Kostabon 14, Ruseler 14, Joubert 7 listings) have sites outside the cloud network list, economic.cw answers 403, and SeriDomi photos carry the banner. Fix: add the six agency domains to the cloud environment's allowed list (docs/05 "Network access").
5. The map endpoint `/api/real-estate/map` returns at most 400 listings; `/api/real-estate` (paged) has 567 active on 8 Nov (365 for sale, 202 for rent). The "400 homes" milestone in state/radar.json was the cap, not a real count; the 500 milestone is already passed. Counts for posts must come from the paged endpoint. `scripts/market_scan.py` reads the map, so its home picks miss 167 listings (a script fix, needs the Product Lead's OK as a rules/tools change).
6. Data issues for merkado-cw: SeriDomi 2023 Kia Picanto is XCG 18.500 at the source and XCG 19.000 on merkado.cw; CuraCars Navara 2009 (260 km) and Amarok 2013 (16 km) show placeholder mileage at the source; Moret's Cocolora photo returns 404 through the merkado.cw image proxy.

7. Product Lead edits (8 Nov): a carousel that mixes homes for sale around XCG 1 million with a rental reads as "weird", and so does a car carousel with only two cars. From now on: one listing type and one price band per real estate carousel, and never a two-listing carousel; when only two sellers pass, use a single post for the strongest listing (a verified price drop or a native listing) instead.

Change to try next week: none to the schedule (data rule). Content test: a single verified price-drop feed post (Fri) against last week's three-car carousels; compare reach, saves, shares and clicks.
Result of last week's change (SUV theme with a wide price range vs a narrow bargain theme): SUVs reached Instagram 5 and Facebook 3 with 3 clicks; the city cars bargain carousel reached Instagram 9 and Facebook 4 with 0 clicks. Not conclusive at this size: slightly more reach for the bargain theme, more clicks for the SUVs.

## 1 Nov 2026: weekly run, week 44 numbers

Numbers (Metricool, 29 Oct to 1 Nov; first three days of posting):
- Launch post "The comment section" (Thu 12:15): Instagram reach 27, 59 views, 6 likes, 1 save; Facebook reach 4, 12 impressions, 1 click.
- City cars carousel (Fri 12:15): Instagram reach 8, 29 views, 2 likes; Facebook reach 2.
- Followers: Instagram 13 to 14. Story numbers not reported by Metricool yet.

Findings:
1. Too little data to judge days, times or series (week 1 of 3 of the "collect, change nothing" rule). Metricool has no Instagram best-time data yet; its Facebook best-time map peaks at 10:00 to 12:00 on weekdays (Wednesday strongest) and drops after 19:00, which supports the 12:15 feed slot.
2. The brand post out-reached the listing carousel about 3 to 1 on Instagram, as hypothesis 2 expected; one pair of posts is not proof.
3. Pre-flight caught a rented listing: RE/MAX marks some rentals "rented" on its own page (hr2192, hr2121) while merkado.cw still lists them as active. Data issue for merkado-cw. The RE/MAX check must look for the "rented" label next to the price, not only a 200 page.
4. The scan's home "price drops" on 31 Oct and 1 Nov (about 0.2% on most RE/MAX listings) are EUR to XCG exchange-rate moves, not real drops. Treat home changes under 1% from EUR-priced agencies as noise. The scan's "cheapest SUV / pickup on Merkado" lines skip Economic Auto Center cars (no mileage), so they can be wrong; check the full list before saying "cheapest".
5. Supply limits the weekly mix: with one listing per seller per week, two carousels plus two stories need seven sellers. This week only six had usable listings (SeriDomi's photos all carry the banner, Monumentenzorg lists commercial spaces), so the Thursday story was left open. Economic Auto Center's site now answers (it returned 403 on 28 Oct), which adds a seller.

6. Product Lead edit (2 Nov): he swapped the Chrysler 200 story because the native listing dated from 24 May and might no longer be for sale. Native listings have no source page to check, so an old one can look active while it is gone. From now on: prefer native listings published in the last 60 days; for older ones, say the age in the approval message so he can judge.

Change to try next week: none to the schedule (data rule, weeks 1 to 3). Content test: an SUV theme with a wide price range (XCG 14.900 to 119.900) against last week's narrow bargain theme; compare reach, saves and shares.
Result of last week's change: none set yet.
Also: the island map (T08) cannot be redrawn from a cloud run because CARTO tiles are blocked by the proxy. Monday used the neighbourhood list (M4). For a map next month, add `basemaps.cartocdn.com` and `tiles.basemaps.cartocdn.com` to the cloud environment's allowed domains, or render it on the Product Lead's PC.

## 29 Oct 2026: links in stories

- Instagram's API does not allow link stickers (or other interactive stickers) on stories that publish automatically. Metricool can only do it as a manual post: it sends a phone notification and the person finishes the story in the Instagram app. Our stories stay automatic, without link stickers; the story names the listing and merkado.cw, and the bio link carries the clicks. Revisit if Meta adds link stickers to the API. Sources: help.metricool.com "Content planning: full guide & FAQs" and "Schedule and Post on Instagram".

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
