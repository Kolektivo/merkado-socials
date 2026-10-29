# 04 Design system: Templates v2 (29 Oct 2026)

Approved by the Product Lead on 28 and 29 Oct 2026 after design rounds 6 to 11. Fill templates; never redesign them without a new approved round. Unique posts are the exception: each gets its own new design inside this system.

Figma file: `Km2x15bnTmb9R8LbnEvQTT` ("Merkado Social Imagery"), cleaned up on 29 Oct 2026. Pages: **Templates v2 · 29 Oct 2026** (`88:182`), **Posts · <ISO week>** (real posts, one page per week), **Posts · upcoming drafts** (`88:185`), **One-off library** (`88:186`, inspiration only), **Brand assets** (`10:18`, logo, chip and card components), **Product Lead · iterations** (`88:187`, the Product Lead's own work; never edit). Old rounds were deleted; Figma version history still has them.

## Templates

`state/templates.json` holds every node id; it wins if this table and the file disagree.

| ID | Template | Node | Use |
| --- | --- | --- | --- |
| C1 | Carousel cover · violet | `88:210` | Car or real estate carousel cover, violet grid slot |
| C2 | Carousel cover · paper | `88:227` | Same, paper grid slot |
| C3 | Listing slide · car | `88:244` | Paper, photo 936 x 700, name, price, specs, Via |
| C4 | Listing slide · home | `88:259` | As C3, neighbourhood as title |
| C5 | End slide · violet | `88:274` | Search all <count> on merkado.cw, dated |
| S1 | Story · style C | `88:281` | Violet, reason as headline (listings with a reason) |
| S2 | Story · style B | `82:212` | Paper, price as headline (bargains, price drops) |
| M1 | The comment section | `37:3` | Brand, paper only |
| M2 | List on Merkado | `37:80` | Sellers, violet |
| M3 | Island Index · map | `37:91` | Monthly, paper only |
| M4 | Island Index · neighbourhoods | `37:98` | Live counts, paper |
| M5 | Island numbers / milestone | `37:34` | Counts and milestones |
| M6 | Guide cover | `37:43` | Before you buy, What's new; make a paper or violet version for the grid slot |
| M7 | Guide inside slide | `37:51` | Steps and checklists |

## Unique posts and the one-off library
The library page holds strong earlier designs ("Made to search, not scroll" with comment cards and a search bar, the giant search bar with live neighbourhood counts, the neighbourhoods list, Buy/Rent property cards, story concepts). Use them as a starting point only. Every unique post gets a new composition inside the brand system (colours, type, rounded frames, the .cw tag), so the feed never repeats itself. Sample photos and sample numbers in the library are placeholders: a published post uses only real, checked listings and live, dated numbers.

## Real listing photos (most are landscape)

Current approach (28 Oct 2026, no AI): carousel slides put the photo in a rounded 936 x 700 frame on paper (most dealer and agency photos are 4:3 and fit whole; wider photos lose only empty space at the sides; overlay watermarks like mobilox stay whole, background wall signs may be trimmed). Covers and end slides are violet, headline in Display L, with one oversized .cw tag from the logo behind the content (Product Lead's design, Figma 78:533): upright, about 2086 x 1115, placed at x 345, y 408 so only its rounded point shows from the bottom right, white at 7%. Same on covers and end slides. Stories: two styles (Product Lead, 29 Oct 2026). Style C (Figma 82:239): violet with the background shape, the reason as a Display L headline ("7 seats, under XCG 20.000"), photo 936 x 702, then name and key fact in Post/Title and the price in Display M, Via right-aligned on the price line. Style B (Figma 82:212): paper, the price as a Display XL headline in Violet 500, name below, photo 936 x 702, specs and Via; for bargains and price drops. Both centred between y 340 and 1580; prefer listings with 4:3 or taller photos; never two photos of different heights; full photo (T10) only for photos that are already tall. Reference: Figma page Round 9 (car carousel 75:183 to 75:282, rental carousel 75:296 to 75:391, story 80:302) until the templates are locked again.

Dealer and agency photos are 16:9 or 4:3, often with a watermark or a banner. Two ways to fill the frame, in this order:

### A. AI-expanded photo (switched off on 28 Oct 2026: pay-per-photo is not scalable; Weave's free plan allows 2 runs only. Kept here for reference)
Merkado uses AI, so listing photos may be expanded with AI to fill the 4:5 or 9:16 frame. Guardrails, all required:
1. Expand outward only. Every original pixel stays as it is; the car or the property is never added to, removed from, redrawn or "improved".
2. Only background continues: sky, wall, ceiling, floor, road, garden, sea. No new cars, people, signs, text, logos or buildings.
3. Check the result at full size before using it. If anything in rule 1 or 2 is broken, use version B instead.
4. Set `isAiGenerated: true` on the Metricool post (Instagram asks for AI-edited photos to be labelled), and add this line to the caption disclaimer: "Background extended with AI; the car (or home) is shown as photographed."
5. Tool: an image-expand (outpainting) model through Figma Weave (`weave_find_model`, `weave_upload_asset`, `weave_run_model`). Needs the Product Lead's Figma account linked to Weave. Figma's `generate_image` cannot expand an existing photo.
6. Layout with an expanded photo: use T10 (story) or T02 (feed) and place the expanded photo full-bleed, card where the template has it.

### B. Blurred backdrop (fallback, always available)
T11 and T12 place the whole photo, full width and uncropped (height from the photo's own ratio, at most 700 px on feed), over a backdrop of the same photo blurred (layer blur 120) under a Surface dark shade at 62%. Story: photo starts 56 px below the card. Feed: photo at y 150, card bottom at y 1278.
Note: in the locked T11 frame the "Backdrop shade" layer is hidden. Turn it on in every copy (bright backdrops otherwise make the white logo unreadable). Fixing the locked frame itself needs the Product Lead's OK.

### Always
- Crop only to remove empty space or a banner strip at the edge. Never crop into the car or the building.
- Keep dealer watermarks as they are (they are the seller's credit). Skip photos where a banner covers the subject.
- Prefer the first photo; use another photo of the same listing if the first is weak.
- AI images that show no specific listing (brand posts) are fine with `isAiGenerated: true`. AI never creates a listing that does not exist.
- Long car titles wrap to two lines inside the card (component width 824). Make and model in ink, variant in grey.

## Grid and type

- Margins 72 px. Logo top left at (72, 72), 40 px tall on feed; stories start at y = 250 (Instagram top safe zone) and keep text above y = 1580 (bottom safe zone).
- Status chip right-aligned to the 72 px margin, centred on the logo line.
- Headline starts at y ≈ 164 on feed posts (T08 is the exception: bottom left).
- Type: Inter Display Semi Bold for headlines (160, 128, 96, 64), Inter for interface text (40, 32, 28). Display tracking about -3%.
- Text styles and colour styles are in the file (`Post/...`). Use them; do not set raw values.

## Colours (from merkado.cw `app/globals.css`)

| Token | Hex | Use |
| --- | --- | --- |
| Violet 500 | `#564EE4` | Brand ground, accents, map pins |
| Violet 50 | `#EEEDFC` | Soft ground, map sea |
| Violet 100 / 200 | `#CBC8F7` / `#B1AEF3` | Secondary text on violet |
| Violet 700 / 900 | `#3D37A2` / `#242160` | Text on Violet 50, deep accents |
| Surface dark | `#141414` | Ink, dark grounds, photo shade |
| Background | `#FAF9F8` | Paper ground |
| White | `#FFFFFF` | Cards |
| Greys | `#F0F0F0` `#E8E8E8` `#DEDEDE` `#CECECE` `#929292` `#717171` `#575757` | Lines, muted text |
| WhatsApp green | `#25D366` | Only on WhatsApp buttons |

No other colours. No gradients, stickers, grain or invented icons. All text pairs pass WCAG AA.

## Cards and components

- Listing card: radius 32, shadow 0/20/56 at 14%, specs as text with 2 px dividers (no icons).
- Price format: `XCG 89.900,-` (dot for thousands, comma-dash). Mileage `108.199 km`.
- Title: make and model in ink, trim or model variant in grey. Leave the trim out when the source "trim" is not a trim (a colour, a dealer code).
- Chip labels: `Just added` (published on merkado.cw within 7 days of the post date), `For sale`, `For rent`, `Price drop` (only with a verified earlier price), `Featured` (only paid Sentoo Featured with the owner's consent).
- Via line: `Via <Seller>` with the seller name in Semi Bold. Private sellers: `Via a private seller` (never their name).

## Map (T08)

Drawn from CARTO `carto.streets` vector tiles (OpenStreetMap data), zoom 13, island bbox lon -69.165 to -68.735, lat 12.035 to 12.392, width 984 px at x 48, top 170. Sea Violet 50, land white with a soft violet shadow, roads in greys, pins Violet 500 r 6.5 with a 2.5 white ring. Pins only for listings with coordinates on land. Always print "Map data © OpenStreetMap · © CARTO".
