# merkado-socials

The working home of Merkado's social media agent (Claude). It plans, designs, drafts and reviews posts for the Merkado Facebook Page and Instagram (@merkado.cw). The Product Lead approves posts in Metricool.

Nothing in this repo touches the merkado.cw app, its database or its users. It only reads public merkado.cw pages and the merkado-cw repository.

## Start here

Open `AGENTS.md`, then `docs/00-docs-index.md`. Everything project-specific is in `config/brand.json`. The procedures are skills in `.claude/skills/` (`/weekly-run`, `/daily-check`, `/make-post` in Claude Code).

## How it runs (short version)

1. **Every Sunday afternoon** a scheduled Claude session runs the weekly-run skill: reviews last week's numbers, re-decides days and times, plans, picks live listings, renders from the locked Figma templates and puts drafts in Metricool.
2. **The Product Lead** opens Metricool and schedules the drafts (about 10 minutes a week).
3. **Every morning** the daily-check skill re-checks listings in upcoming posts, pulls any post whose listing is gone, and looks for product updates and milestones.

## Reusing this for another project

Copy the repo, replace `config/brand.json`, the Figma templates (`docs/04-design-system.md`, `state/templates.json`) and the content rules in `docs/03-content-playbook.md`. The skills and structure stay the same.
