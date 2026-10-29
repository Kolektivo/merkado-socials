---
name: make-post
description: Make one Merkado social post end to end (pick or receive content, pre-flight check, render from the locked Figma template, export, host, caption, Metricool draft, log). Use for any single post or Story.
---

# Make one post

Read `AGENTS.md`, `docs/03-content-playbook.md` (sections 4 to 8) and `docs/04-design-system.md` first.

1. **Content.** Listing post: pick per playbook section 7 and run the pre-flight. Data post: pull live numbers and note the date. Guide: use only the published merkado.cw Resource. News: only what is live on merkado.cw.
2. **Template.** Choose from `state/templates.json`. Landscape listing photo: rounded-frame layout (design system, "Current approach"); no AI expansion. Otherwise T11 (story) or T12 (car feed).
3. **Render.** Follow docs/05 "How a post is made", Design (Figma). Duplicate the template onto the page `Posts · <ISO week>`, replace content only, check the screenshot for overflow and clipping.
4. **Export and host.** JPG to `assets/<YYYY>-W<ww>/`, commit and push, confirm the raw GitHub URL returns 200.
5. **Caption.** Use the skeleton in playbook section 6. Alt text. First comment with the UTM link. Add the AI line if the photo was expanded. Write it to `captions/<YYYY>-W<ww>.md`.
6. **Metricool.** Create the draft (or send for review) per docs/05 "Metricool". Set `isAiGenerated` correctly.
7. **Log.** One row in `state/posts.csv`. Update `docs/10-calendar.md` status.
