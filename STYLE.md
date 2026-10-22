# Merkado social style: Templates v1 (locked 22 Oct 2026)

Approved by the Product Lead on 22 Oct 2026 after five design rounds. Do not change the look without a new approval round. Fill templates; never redesign them.

Figma file: `Km2x15bnTmb9R8LbnEvQTT`. Page: **Templates v1 · Locked (22 Oct 2026)** (page id `37:2`). Brand components live on the page **Brand assets** (`10:18`).

## Templates

| ID | Name | Node | Size | Use |
| --- | --- | --- | --- | --- |
| T01 | Brand · The comment section | `37:3` | 1080×1350 | Brand posts. Grey struck-through comments, the answer in Violet 500. Swap the comment lines per edition (cars, homes). |
| T02 | Listing · Car (vertical photo) | `37:15` | 1080×1350 | Only for portrait photos (rare). Full photo, listing card at the bottom. |
| T03 | Listing · Property | `37:21` | 1080×1350 | Violet ground, big headline, framed photo, price. |
| T04 | Island numbers | `37:34` | 1080×1350 | Live counts, dated and sourced. Also milestones. |
| T05 | Guide · Cover | `37:43` | 1080×1350 | Surface dark, editorial headline. Guides and What's new covers. |
| T06 | Guide · Inside slide | `37:51` | 1080×1350 | Step, checklist, progress bar. Carousel slides after T05. |
| T07 | List on Merkado | `37:80` | 1080×1350 | For sellers. Violet, website skeleton cards and buttons. |
| T08 | Find home · Island map | `37:91` | 1080×1350 | Island map with every pinned listing, headline bottom left. Re-render the map monthly. |
| T09 | Find home · Neighbourhoods | `37:98` | 1080×1350 | Top six neighbourhoods with live counts. |
| T10 | Story · Listing (vertical photo) | `37:134` | 1080×1920 | Only for portrait photos. Full-bleed photo, card in the sky. |
| T11 | Story · Listing (landscape photo) | `45:136` | 1080×1920 | Default story for real listing photos. Sample: 2016 Land Cruiser Prado. |
| T12 | Listing · Car (landscape photo) | `45:546` | 1080×1350 | Default feed post for real car photos. Sample: 2023 Kia Soul. |

`state/templates.json` holds the current node id of every template, including T11 and T12. If a node id there and in this table disagree, `state/templates.json` wins.

## Real listing photos (most are landscape)

Dealer and agency photos are 16:9 or 4:3, often with a watermark or a banner. Two ways to fill the frame, in this order:

### A. AI-expanded photo (preferred, approved by the Product Lead on 22 Oct 2026)
Merkado uses AI, so listing photos may be expanded with AI to fill the 4:5 or 9:16 frame. Guardrails, all required:
1. Expand outward only. Every original pixel stays as it is; the car or the property is never added to, removed from, redrawn or "improved".
2. Only background continues: sky, wall, ceiling, floor, road, garden, sea. No new cars, people, signs, text, logos or buildings.
3. Check the result at full size before using it. If anything in rule 1 or 2 is broken, use version B instead.
4. Set `isAiGenerated: true` on the Metricool post (Instagram asks for AI-edited photos to be labelled), and add this line to the caption disclaimer: "Background extended with AI; the car (or home) is shown as photographed."
5. Tool: an image-expand (outpainting) model through Figma Weave (`weave_find_model`, `weave_upload_asset`, `weave_run_model`). Needs the Product Lead's Figma account linked to Weave. Figma's `generate_image` cannot expand an existing photo.
6. Layout with an expanded photo: use T10 (story) or T02 (feed) and place the expanded photo full-bleed, card where the template has it.

### B. Blurred backdrop (fallback, always available)
T11 and T12 place the whole photo, full width and uncropped (height from the photo's own ratio, at most 700 px on feed), over a backdrop of the same photo blurred (layer blur 120) under a Surface dark shade at 62%. Story: photo starts 56 px below the card. Feed: photo at y 150, card bottom at y 1278.

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
- Via line: `Via <Seller>` with the seller name in Semi Bold.

## Map (T08)

Drawn from CARTO `carto.streets` vector tiles (OpenStreetMap data), zoom 13, island bbox lon -69.165 to -68.735, lat 12.035 to 12.392, width 984 px at x 48, top 170. Sea Violet 50, land white with a soft violet shadow, roads in greys, pins Violet 500 r 6.5 with a 2.5 white ring. Pins only for listings with coordinates on land. Always print "Map data © OpenStreetMap · © CARTO".
