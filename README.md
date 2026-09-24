# The Jar of Life — website

Static website for **The Jar of Life**, a solo mobile game studio
([thejaroflife.com](https://thejaroflife.com)). Plain HTML + CSS — no build
step, no framework, no backend, no database.

## Structure

```
index.html              Homepage: hero, featured game, fair play, about, contact
games/rune-raid.html    Rune Raid game page
css/styles.css          Shared styles for every page
assets/img/             Images (logo, cover art, screenshots)
scripts/deploy.py       Uploads the site to Fasthosts over FTP(S)
.env.example            Shape of the FTP credentials (copy to .env)
```

Only `index.html`, `games/`, `css/` and `assets/` are uploaded when deploying.
Everything else (README, scripts, `.env`, git files) stays on your machine.

### Why styles live in `css/styles.css`

- **Split out (current):** there are now two pages sharing one look. One CSS
  file means a colour or font change happens once, and browsers cache it
  between pages.
- **Single-file (the original mockup approach):** simplest possible, but every
  new page duplicates the styles and they drift apart.
- With a second page already here and more games coming, a shared stylesheet
  is the better trade.

## Local preview

- **Quickest:** double-click `index.html` to open it in your browser. All links
  are relative, so navigation works straight from disk.
- **Closer to the real server** (optional), from this folder:

  ```
  python -m http.server 8000
  ```

  Then open <http://localhost:8000>.

## Deploying to Fasthosts

The deploy script uses Python's standard library only, so there's nothing to install.

### Once domain + hosting are live

1. Copy the example credentials file:
   - Windows: `copy .env.example .env`
   - macOS/Linux: `cp .env.example .env`
2. Fill in `.env` with the FTP details from the Fasthosts control panel:
   `FTP_HOST`, `FTP_USER`, `FTP_PASSWORD`, `FTP_PORT` (usually `21`).
   Check `FTP_REMOTE_DIR` too. Fasthosts Linux hosting normally uses `htdocs`.
3. Preview what will be uploaded (no connection is made):

   ```
   python scripts/deploy.py --dry-run
   ```

4. Deploy:

   ```
   python scripts/deploy.py
   ```

5. Visit https://thejaroflife.com and check both pages.

> **Status:** hosting isn't live yet, so the script has **not** been run
> against a real server. The first real deploy is the test. If it fails on
> TLS, set `FTP_TLS=false` in `.env` and try again.

`.env` is git-ignored and must never be committed.

### Why Python for the deploy script

- **Python (chosen):** `ftplib` is built in, with FTPS (encrypted) support.
  No dependencies, and it runs the same on Windows, macOS and Linux.
- **PowerShell:** built into Windows, but its FTP support (`WebRequest`) is
  deprecated and awkward for uploading whole folders. It's also Windows-only.
- **Node:** would need an npm package (`basic-ftp`), which means a
  `package.json` and `node_modules` for a site that otherwise has no tooling.

## Email

- `support@thejaroflife.com` is public and linked on the site.
- `admin@thejaroflife.com` is for accounts and registrations only. It's
  intentionally not shown on the site, to keep it away from spam scrapers.

## Content still needed

Placeholders are marked `PLACEHOLDER` (visible on the page) or
`DRAFT COPY` / `TODO` (HTML comments). Search the files for those words to find them.

- [ ] **Logo.** SVG preferred, otherwise a transparent PNG of at least 512×512.
      It replaces `assets/img/logo-placeholder.svg`, which is also used as the favicon.
- [ ] **Rune Raid cover art.** Landscape, around 1600×1000. It's used on the
      homepage and the game page.
- [ ] **Social share image.** 1200×630, for `og:image` link previews. This can be
      a crop of the cover art.
- [ ] **Rune Raid screenshots.** Four portrait phone screenshots.
- [ ] **Copy review:** hero tagline, Rune Raid pitch and feature cards, fair
      play points, about text. All of it is draft.
- [ ] **Launch details:** platforms, release date, App Store / Google Play URLs.
