# Rules for Claude working on thejaroflife.com

Read `WEBSITE_PLAN.md` first for context (stages, status, what's still needed).

## How publishing works
- The live site is uploaded from Nicol's PC: `C:\CLAUDE_STUFF\thejaroflife-site`.
  FTP details are in the local, git-ignored `.env` there. Nothing publishes
  automatically, and merging on GitHub does not change the live site.
- Stage 1 (now): `python scripts/deploy.py --coming-soon`
  Stages 2-3: `python scripts/deploy.py`

## Publishing the live website — always follow
- The only command that publishes is: **"Publish live website"**.
  Words like "merge", "go", "ship it" or "looks good" are NOT approval to publish.
  If Nicol says something like that, ask whether they mean "Publish live website".
- When Nicol says "Publish live website", first reply with exactly:
  **"Are you sure? This will update the LIVE website."**
  followed by a short bullet summary of exactly what will change compared with
  the version currently live (pages, text, images added/changed/removed).
  Only continue after they answer yes.
- Then, on the PC: `git pull` (to pick up changes made in other chats), run the
  deploy for the current stage, check it succeeded, and commit + push any
  local changes so GitHub keeps a backup copy.
- When the live website has been updated and the check has confirmed it (every
  uploaded file matches on the live server), display this line on its own:
  **\*\*\* LIVE WEBSITE UPDATED \*\*\***
  Show it only after a verified success, for any change to the live server
  (a deploy or a file deleted there). If the upload or the check fails, do not
  show it; report the failure instead.
- **Cloudflare caching — Nicol never has to purge anything.** Cloudflare (and visitors'
  browsers) keep copies of images, CSS and robots.txt for up to 4 hours; HTML pages are
  never cached. So whenever a change replaces an image or the stylesheet, give the changed
  file a NEW filename (e.g. `jar-of-life-logo-v2.jpg`), update every page that references
  it, and add it to `COMING_SOON` in `scripts/deploy.py` when stage 1 needs it. Never
  overwrite a cached file under its old name. Fixed-name files that can't be renamed
  (`robots.txt`, `app-ads.txt`, `sitemap.xml`) may show the old version for up to 4 hours;
  say so in the publish summary — no action for Nicol.
- **How to verify a live update behind Cloudflare.** Compare each uploaded file with the
  copy on the Fasthosts server directly (HTTP to 77.68.64.40 with `Host: thejaroflife.com`),
  because Cloudflare rewrites the support@ email link (email obfuscation) and serves cached
  copies of images. Then load the public https page and confirm the changed text is there.
  Both must pass before showing the LIVE WEBSITE UPDATED line.
- A cloud/web session can't reach the PC or Fasthosts. It can only prepare
  changes and push them to GitHub; publishing happens in the PC session.

## Drafts and previews
- Make changes to the local copy first. The live site is untouched until
  "Publish live website" is confirmed.
- For every draft, show Nicol a preview: the page opened locally in the browser,
  or (from a cloud session) the rendered page plus screenshots at phone (375px)
  and desktop (1280px) widths, viewable in the Claude mobile app.

## Other standing rules
- Website only: never change the game repo (`NicolJarvie/RuneRaid`).
- The game's name is **Runic Raid** (not "Rune Raid").
- Never put the FTP password in chat, commits or any tracked file. It lives
  only in the local `.env`.
- Firm rule: no social posting or store-listing work until Runic Raid is fully
  tested and all supporting content is built (see `WEBSITE_PLAN.md`).
