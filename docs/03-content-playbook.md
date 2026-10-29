# 03 Content playbook

Status: Active, v1 (22 Oct 2026). Owner: Product Lead (Enrique). Operator: Claude (scheduled runs).
This file is the agent's operating manual. Read `AGENTS.md` first, then this file, then the docs and `state/` files it points to.

## 1. Goal

See `docs/01-goals-and-audience.md`.

## 2. Sources of truth (in this order)

1. Live merkado.cw data and pages (what is really live today).
2. The merkado-cw repo on GitHub `Kolektivo/merkado-cw`, branch `main`: `AGENTS.md`, `docs/02-scope-and-decisions.md`, `docs/09-current-state.md`, `docs/10-execution-roadmap.md`. Read only. Never write to it.
3. This repo: docs/03-content-playbook.md, docs/04-design-system.md, docs/10-calendar.md, docs/11-learnings.md, `state/`.
4. Chat summaries are never a source of truth.

If a source conflicts with this playbook (for example a feature is described in docs but not visible on merkado.cw), do not post about it. Note the conflict in the run report.

## 3. Channels and formats

| Channel | Formats | Notes |
| --- | --- | --- |
| Facebook Page `merkado.cw` | Feed image or carousel 1080×1350, Story 1080×1920 | Main stage on Curaçao (CBS Social Survey 2025: Facebook 78%, Instagram 38.5%). |
| Instagram `@merkado.cw` | Same assets, same day | Carries the look. |
| Later | Reels (launch video), TikTok, WhatsApp Channel, LinkedIn for dealers and agencies | Only after the Product Lead approves each one. |

One Metricool post covers both Facebook and Instagram (same image, same caption) unless a format needs a split.

## 4. Post types (what we post)

Weekly rhythm: Monday feed (rotating type below), Tuesday story, Wednesday real estate carousel, Thursday story, Friday car carousel.

| Post type | Format | When | What it is |
| --- | --- | --- | --- |
| **Car carousel** | Violet cover + 3 to 5 cars on paper + violet end | Every Friday | One car per seller, rotating themes (section 7). Bargains at least every other week. |
| **Real estate carousel** | Same, with homes | Every Wednesday | One home per agency, rotating themes (section 7). Never mixed with cars. |
| **Listing story, style C** | Violet, the reason as the headline, photo, name and price | Tuesday or Thursday | For a listing with a reason: 7 seats, just added, electric, native listing, popular area. |
| **Listing story, style B** | Paper, the price as the headline, photo, specs | Tuesday or Thursday | For bargains and verified price drops. Stories alternate B and C like the feed alternates paper and violet. |
| **The comment section** | T01 brand post | Monday, about once a month | "Price? PM. Still available?? Or just search." Cars and homes editions. |
| **Before you buy** | T05 cover + T06 slides | Monday, about once a month | Guides built only from published merkado.cw Resources (used car checklist, buying a house, mortgages, insurance, ownership transfer, importing a car). |
| **Island Index** | T08 map, T09 neighbourhoods, T04 numbers | Monday of the first week of each month | Live, dated numbers: every home on the island map, top neighbourhoods, cars by type and make. |
| **What's new** | T05 + T06 or T04, plus a story | Monday, or next day for big news | Merkado features once they are live (business pages, payments for every seller, car price history, Property Match, new dealers or agencies). |
| **List on Merkado** | T07 | Monday, about once a month | For sellers: free to list, 2 listings included, WhatsApp contact. Only claims true on /pricing that day. |
| **Milestones** | T04 | When a threshold is crossed | For example 250 or 300 cars, 400 homes, 1.000 listings. |
| **Payments launch arc** | Feed, carousel, story, Reel | The day payments open to every seller | See docs/10-calendar.md Phase 2. |

Later, each only after the Product Lead approves it: Reels (launch video, phone-shot car hunts), partner spotlights with dealers who opt in, December holiday angles, Papiamentu and Dutch versions.

### The grid (Product Lead, 29 Oct 2026)
The Instagram profile shows feed posts three to a row, so the first image of every feed post alternates with the feed post before it: paper, violet, paper, violet. Because a row has three posts, strict alternation keeps the whole grid a checkerboard, whichever post is newest. Stories do not count; they alternate style B (paper) and C (violet) on their own.
- Carousel covers, guide covers, What's new and List on Merkado exist in a paper and a violet version. The comment section and the island map are paper only, so they go in paper slots.
- When an extra post (news, a unique post) is inserted, every later post flips so the alternation holds. Check the order against the last published post before scheduling.
- Never two near-identical designs within three posts of each other (for example two comment-section posts).

### Unique posts
Besides the recurring types, the feed gets one-off posts with their own design, like the launch post. At most two a month, each shown to the Product Lead with two options before it is scheduled, and slotted into the paper/violet alternation. Start from the One-off library in Figma (page `88:186`: "Made to search, not scroll" with comment cards, the giant search bar, the neighbourhoods list, Buy/Rent property cards, story concepts), but never reuse a design as is: every unique post gets a new composition in the brand system, and the agent keeps iterating new ideas (Product Lead, 29 Oct 2026).
- **Merkado moments:** launches (the payments launch, Property Match going public), milestones (300 cars, 1.000 listings, first 100 followers), a year-in-review in January.
- **Island moments:** Carnival (February), Seú (Easter Monday), Dia di Himno i Bandera (2 July), Dia di Pais Kòrsou (10 October), Sinterklaas (5 December), Christmas and New Year. Light and local, always tied back to cars or homes, never a sales push on a sensitive day.
- **Campaign posts:** new takes on "Made to search, not scroll." (for example "The comment section" editions or "Scroll vs search" comparisons from earlier design rounds).

Mix per 4 weeks: 8 listing carousels (4 cars, 4 homes), 8 stories, 4 Monday posts (roughly 1 comment section or List on Merkado, 1 guide, 1 Island Index, 1 What's new or extra), plus news when the radar finds it. Adjust with docs/11-learnings.md.

## 5. Weekly rhythm (Curaçao time, America/Curacao, UTC-4)

| Day | Time | Slot |
| --- | --- | --- |
| Monday | 12:15 | Feed: brand, guide, data or seller post (see docs/10-calendar.md) |
| Tuesday | 19:00 | Story: a live listing |
| Wednesday | 18:30 | Feed: real estate carousel (one listing per agency) |
| Thursday | 19:00 | Story: a live listing (the other category from Tuesday) |
| Friday | 12:15 | Feed: car carousel (one listing per seller) |

### Finding the best days and times (every weekly run)

These slots are a starting point, not fixed. Every Sunday the agent re-decides days and times from two signals:

1. **Metricool best time to post** (`getBestTimeToPostByNetwork`) for Facebook and Instagram separately, over the last 28 days: which weekdays and hours our audience is most active.
2. **Our own results**: reach, saves, shares and link clicks of every post from the last 4 to 8 weeks, grouped by weekday and time block (morning, lunch, evening) and by series, so a strong series is not mistaken for a strong day.

Rules for changing the schedule:
- Weeks 1 to 3: collect data, change nothing (too little data on a new account).
- From week 4: move a slot only when both signals point the same way, or when one slot beats the others by at least 30% on average reach over 3 or more posts.
- Change one thing per week (one day or one time), so the effect can be measured. Keep 3 feed posts and 2 Stories a week unless docs/11-learnings.md shows more helps.
- Facebook and Instagram may get different times. If they differ by more than 2 hours, schedule the network posts separately.
- Monthly: test one new slot (for example Saturday morning or Sunday evening) with a listing post and compare.
- Write every change and its result in docs/11-learnings.md, and update the table above and docs/10-calendar.md.

## 6. Voice and captions

- English only for now (Product Lead, 10 Oct 2026). Papiamentu and Dutch later.
- Short, warm, plain, local. Talk like a helpful neighbour who knows the market, not like an ad.
- Lead with the useful thing (price, place, what it is). No hype words ("amazing", "dream", "don't miss out"), no em dashes, no ALL CAPS, at most one emoji and only if it adds meaning.
- Never invent facts, numbers, quotes, testimonials or partners. Every number comes from live data with a date.
- No hashtags (Product Lead, 28 Oct 2026: they look cheap). Instagram and Facebook search read the caption text, so name the plain words people search for in the sentences themselves: the make and model, "car", "house", "for rent", the neighbourhood, "Curaçao".
- Links: no URL in the caption. Put the full link with UTM in the first comment: `https://merkado.cw/<path>?utm_source=social&utm_medium=metricool&utm_campaign=<series-slug>&utm_content=<post-id>`. The caption ends with "Link in the first comment" on listing posts, or "Search it on merkado.cw" on brand posts.
- Alt text on every image: one plain sentence describing what is shown.

### Caption skeletons

Listing (car):
```
<Year> <Make> <Model>, <mileage> km, <fuel>, <gearbox>.
XCG <price>, listed by <Seller>.
<One useful line: what it suits, from the listing itself, never invented.>

Details come from <Seller>'s listing. Always check the original listing and contact the seller for official details.
Link in the first comment.
```

Listing (real estate): same, with type, bedrooms, bathrooms, m², neighbourhood, sale or rent.

Brand / data / guide: a hook line, two or three short lines of substance, a plain call to action.

## 7. Listing posts: picking, checking, crediting

### Strategy: every listing post has a reason
A listing is never posted just because it is there. Each pick has one clear angle, and the angle shows in the post (chip, headline or first caption line). Run `python scripts/market_scan.py picks car` and `... picks home`: it ranks live listings and prints the reasons. Angles, strongest first:
1. **Native listing** (listed on Merkado itself, private or business). Strategic: shows Merkado is a place to sell, not only a mirror of dealer sites.
2. **Price drop**, only when verified: our own dated price log (`state/market/price-changes.csv`, written by the daily snapshot) or the public price trail on a real-estate Listing Score, and confirmed at the source. Chip `Price drop`, caption "Was XCG X on <date>, now XCG Y."
3. **Just added** (on merkado.cw for 7 days or less on the post date).
4. **Below similar cars on Merkado**, only with at least 4 comparable live cars (same make and model, within 2 years), clean data on all of them, and the price checked at the source. Say it as a dated fact ("XCG 4.000 below the middle price of 6 similar Picantos on Merkado today"), never "good deal", "cheap" or a valuation.
5. **Bargains lead.** People on Curaçao love a bargain (Product Lead, 28 Oct 2026), so price angles come first among the demand angles: price drops, under XCG 10.000 or 15.000, the cheapest SUV, sedan or pickup on Merkado this week, rentals under XCG 3.000. Always as dated facts with the price.
6. **Demand angles** that people on the island search for: under XCG 15.000, 7 seats for the family, electric and hybrid, pickups for work, rentals under XCG 3.000, popular areas (Blue Bay, Jan Thiel, Otrobanda, Piscadera).
Data flags from the scan (year in the link differs from the listing, no mileage, implausible or placeholder-looking mileage) mean: check at the source, and skip if it still disagrees. Report it as a data issue.

### Formats for listings
- **Story:** one listing. Full photo (T10) only when the seller's photo is already tall (phone photos often are); a wide photo goes in a rounded frame, or two of the listing's own photos stacked. No AI photo extension (not scalable, Product Lead 28 Oct 2026). Two a week, ideally one car and one home.
- **Two round-up carousels a week (Product Lead, 28 Oct 2026): cars on Friday, real estate on Wednesday, never mixed.** Default for scraped listings: cover + 3 to 5 listings + end slide. Scraped stock is shown in bulk, so people see how much is on Merkado and swipe. Themes: "Just added this week", "Under XCG 15.000", "7 seats", "Electric and hybrid", "Rentals under XCG 3.000", "New in Blue Bay". **One listing per seller in a carousel, always** (Product Lead, 28 Oct 2026). When a theme has fewer than 3 clean sellers, widen the theme (any car under XCG 20.000, any rental under XCG 3.000) rather than repeat a seller or mix cars and homes. `scripts/market_scan.py roundup car <theme>` picks one per seller. Slides: paper ground, photo 936 x 700 in a rounded frame, as tall as the photo allows without cutting the car, the home or an overlay watermark; text block centred under it. Cover and end slide violet.
- **Feed single:** only for a listing with its own story: a native listing or a verified price drop.
- Measure which angle and format earns the most saves, shares and link clicks, and shift the mix toward it (section 5 rules on one change per week).

### Theme rotation (car carousel on Friday, real estate carousel on Wednesday)
Bargains lead, but the themes rotate so the feed stays fresh (Product Lead, 28 Oct 2026). `python scripts/market_scan.py themes` lists them; `roundup car <theme>` and `roundup home <theme>` pick one listing per seller.
- **Car themes:** under XCG 10.000 / 15.000 / 20.000, price drops, just added this week, SUVs, pickups, 7 seats for the family, electric and hybrid, nearly new (2 years or less).
- **Home themes:** rentals under XCG 3.000, homes for sale under XCG 500.000, price drops, just added this week, homes with a pool, beach areas (Jan Thiel, Blue Bay, Piscadera, Westpunt).
- A bargain theme at least every other week in each carousel. Never the same theme twice within 3 weeks.
- A theme needs 3 sellers with clean photos and a source that passes the check; otherwise take the next theme.
- Log the theme in the `series` column of `state/posts.csv`. From week 4, weight the rotation toward the themes with the most saves, shares and link clicks.

### Picking
- Only `status = active` listings that merkado.cw shows publicly, with a real price (no "Price on request"), at least one sharp photo that shows the car or property itself, and complete key fields (cars: make, model, year, price; mileage optional but preferred. Real estate: type, price, neighbourhood; bedrooms for homes).
- Prefer variety: different sellers, price ranges and neighbourhoods across a week. Never the same listing twice in 30 days. Never more than one listing from the same seller per week unless they opted in as a partner.
- Use native Merkado listings (listed directly on merkado.cw by private sellers or businesses; `listing_origin = manual` in the API) as well as scraped ones, and prefer a good native listing when there is one (Product Lead, 28 Oct 2026). No written yes is needed. The aim is to show more native listings over time than scraped ones.
- Native listing photos come from merkado.cw itself (the car page lists them); use them through the merkado.cw image proxy like any other photo.
- Look at every photo before picking (use judgement, not a filter). Skip a listing when its photo has a heavy dealer banner or text bar over the image (SeriDomi's top banner, "call us" strips), is a screenshot (black bars, phone status bar), a collage, shows a recognisable private person, or another platform's interface. A subtle corner logo or watermark is fine (Moret's corner logo, mobilox). If another photo of the same listing on merkado.cw is clean, use that one.

### Pre-flight check (when drafting AND again within 48 hours of publishing)
1. The listing is still returned by the merkado.cw API with `status = active`.
2. The original listing (source page) still loads and still shows the listing: not 404 or 410, not redirected to a homepage, not marked sold, reserved or rented. For cars, read the source link from the merkado.cw car page.
3. Price, year and mileage (cars) or price, type and bedrooms (real estate) match between merkado.cw, the source page and the post. If merkado.cw and the source disagree, skip the listing and note it in the run report as a data issue.
4. The photo still loads.
5. Any failure: do not publish. Turn the post back into a draft (`updateScheduledPost` with `draft: true`), log the reason in `state/posts.csv`, and propose a replacement draft.

### Credit and disclaimer
- Every scraped listing shows the seller in the post ("Via <Seller>" on the card) and in the caption ("listed by <Seller>").
- Caption disclaimer on every listing post: "Details come from <Seller>'s listing. Always check the original listing and contact the seller for official details."
- Tag the seller's own Instagram or Facebook account only when it is confirmed in `state/partners.csv`. Never guess a handle.
- Team decision (Oct 2026): we use dealer and agency photos with credit; if a seller asks us to remove a post, remove it within 24 hours and log it in `state/takedowns.md`. Do not post that seller again unless they opt in.

### Privacy and naming
- Never show a private seller's name, phone number or face. Business names are fine. For a private seller the card says `Via a private seller` and the caption says "listed by a private seller on Merkado"; the disclaimer becomes "Details come from the seller's listing on Merkado. Always check the listing and contact the seller for official details."
- **Featured** is reserved for paid Sentoo placements. Organic picks are never called Featured.
- Listing Score is described as listing completeness, never property quality or a valuation.

## 8. Data posts (Island Index)

- Numbers come from the live merkado.cw API on the render date, and the post prints that date and "on merkado.cw".
- The island map (T08) is drawn from OpenStreetMap data via CARTO vector tiles and must print "Map data © OpenStreetMap · © CARTO". Leave out pins that fall in the sea and report them as data issues.
- Counts are "listings" unless the filter really is homes only.

## 9. Product updates and milestones (the radar)

The daily run reads the merkado-cw repo and live merkado.cw to find news worth posting.

### What to watch
- New commits on `main` of `Kolektivo/merkado-cw` since `state/radar.json → last_commit`.
- Changes to `docs/09-current-state.md`, `docs/10-execution-roadmap.md`, `docs/02-scope-and-decisions.md`.
- Live counts (cars, real estate, native listings, businesses) once per day.

### Watchlist (features in the merkado-cw repo, checked daily)
| Feature | Status on 28 Oct 2026 | Post when |
| --- | --- | --- |
| Business accounts (business pages, native listings shown as the business) | Live: first one is Weber & Weber (`/businesses/weber-and-weber`) | Now: What's new post + Story. Name the business only as it appears on merkado.cw; never tag it unless confirmed in `state/partners.csv`. |
| Payments for every seller: Featured (XCG 50, 7 days, 9 spots, native cars) and extra listing (XCG 15) | Built, payments on for the Product Lead only (Sentoo allowlist) | The allowlist is removed and checkout works for any seller: payments launch arc in docs/10-calendar.md. |
| Car Listing Score (public price and sold history per car) | Data is collected, page not public | The history shows on `/car/<slug>`. Then price-drop posts can cite merkado.cw directly. |
| Property Match (describe your situation, get matching homes) | Private beta, behind a password | `SHOW_PROPERTY_MATCH_PUBLICLY` is on and `/find-a-property` opens without a password. Big launch: carousel + Story + Reel idea. |
| Plus and Business plans online | "Request by email" on /pricing | Checkout appears on /pricing. |
| New sources (dealers or agencies added to the scrapers) | Cars: CuraCars, SeriDomi, Carteam, Economic. Homes: RE/MAX, Keller Williams, Moret, Monumentenzorg | A new source appears in the API: "Now on Merkado: <name>" post. |
| New Resources guides (Sanity) | 16 guides | A new guide is published: Before you buy carousel. |

### What counts as news
- A user-facing feature that is **visible on merkado.cw today** (check the page). Code on `main` that is not deployed, behind a flag, private beta or allowlisted is not news yet.
- A milestone crossing a threshold in `state/radar.json → milestones` (for example 300 cars, 500 listings, first business account live, first Featured car).
- Payments go-live: when Featured and the extra listing can be bought by every seller (allowlist removed). This starts the payments launch arc in docs/10-calendar.md.

### What is never news
- Property Match while it is a private beta. Paid features that are not switched on. Merkado Rent Advance or anything from merkado-labs. Internal ops, scrapers, security, refactors, SEO plumbing. Anything only described in docs/private.

### What to do with news
1. Write a one-paragraph brief in the run report: what changed, who it helps, proof it is live (URL).
2. Draft the post(s) as Metricool drafts: T05 cover + T06 slides for a feature, T04 for a milestone, plus a Story. Put them in the next free feed slot or, for big news, the next day at 12:15.
3. Push-notify the Product Lead: "News found: <title>. Drafts ready for your approval."

## 10. How a post is made

Moved to `docs/05-architecture-and-integrations.md` (data sources, Figma, export and hosting, Metricool).

## 11. Approvals

Moved to `AGENTS.md` (what the agent may and may not do, standing approvals).

## 12 and 13. The weekly run and the daily check

Moved to the skills `.claude/skills/weekly-run/SKILL.md` and `.claude/skills/daily-check/SKILL.md`. Making one post step by step: `.claude/skills/make-post/SKILL.md`.

## 14. Run report format

Start with one line: what happened. Then, only if relevant: Drafts created (date, slot, title, Metricool link), Pulled posts (why), News found, Data issues (listing id, what disagrees), Needs you (exact action, where to click). Keep it under 15 lines.

## 15. When something fails

- Never post a guess. Skip, log, report.
- If a tool fails twice, stop that step and report it; do not loop.
- If Figma or Metricool limits are hit, report and finish the rest.

## 16. Takedowns and complaints

Any request to remove a post or stop using someone's photos: the Product Lead forwards it, or it arrives in the run's context. Remove from Metricool if still scheduled; if already published, ask the Product Lead to delete it (the agent cannot delete published posts). Log in `state/takedowns.md`. Add the seller to the do-not-post list in `state/partners.csv`.

