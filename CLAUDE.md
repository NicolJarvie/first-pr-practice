# Rules for Claude working on thejaroflife.com

Read `WEBSITE_PLAN.md` first for context (stages, status, what's still needed).

## Publishing the live website — always follow
- Merging into `main` **publishes the live website** (GitHub Actions uploads it to
  Fasthosts automatically). Never merge into `main` without the steps below.
- The only command that publishes is: **"Publish live website"**.
  Words like "merge", "go", "ship it" or "looks good" are NOT approval to publish.
  If Nicol says something like that, ask whether he means "Publish live website".
- When Nicol says "Publish live website", first reply with exactly:
  **"Are you sure? This will update the LIVE website."**
  plus a one-line summary of what will change. Only merge after they answer yes.
- Every change starts as a draft on a branch / pull request. The live site is
  untouched until it's published.

## Drafts and previews
- For every draft, send Nicol a preview he can view in the Claude mobile app:
  the rendered page(s) plus screenshots at phone (375px) and desktop (1280px)
  widths. They review and ask for tweaks before publishing.

## Other standing rules
- Website only: never change the game repo (`NicolJarvie/RuneRaid`).
- The game's name is **Runic Raid** (not "Rune Raid").
- Never put the FTP password in chat, files or commits. It lives in the
  `FTP_PASSWORD` GitHub secret and in the local, git-ignored `.env`.
- Firm rule: no social posting or store-listing work until Runic Raid is fully
  tested and all supporting content is built (see `WEBSITE_PLAN.md`).
