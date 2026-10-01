# The Jar of Life — Website & Launch Context

Handoff notes from planning done in Claude chat. Read this at session start for context.

## Brand
- Domain: thejaroflife.com (registered, Fasthosts)
- Emails live: support@thejaroflife.com (public), admin@thejaroflife.com (accounts/registrations)
- Logo: made with Gemini, used in site repo already

## Hosting / DNS / SSL — current status
- Fasthosts web hosting is live and ready, but the real deploy hasn't been run yet
- **In progress: migrating DNS + SSL to Cloudflare** (decided against Fasthosts' SSL add-on — free 1st year, ~£37.45/yr after; Cloudflare's is free permanently)
- Cloudflare account registered under admin@thejaroflife.com (Hotmail as recovery)
- Migration steps: Cloudflare account → add domain → verify DNS scan caught existing A + MX records → swap nameservers at Fasthosts → wait for propagation → re-test admin@/support@ email delivery
- Once Cloudflare is confirmed working: fill in repo's `.env` with Fasthosts FTP details, `deploy.py --dry-run`, then real deploy

## Site content still needed (repo TODOs)
- Logo file: SVG or 512×512+ transparent PNG
- Rune Raid cover art: landscape ~1600×1000 (currently have portrait poster art only)
- Social share image: 1200×630
- 4x Rune Raid phone screenshots
- Copy review: hero tagline, Rune Raid pitch, feature cards, fair play points, about text — all draft
- Launch details: platforms, release date, store URLs

## Idea: early "coming soon" placeholder
- Plan to deploy repo as-is (even with draft copy) once Cloudflare's sorted, to get the domain indexed early and test the full pipeline — before the "real" launch

## Games
**Rune Raid: Viking Saga** (renamed from "Rune Raiders" — naming conflict with an old Retro64 game)
- Reverse tower-defense: player controls Viking raiders, steals runes from defended strongholds
- Tap-to-send control scheme
- Playable build on device: level "1-3 Stone Bridge", squad tray, rune ability slots, gold counter, camera controls
- Prototype app icon exists (currently labelled "Runic Raid" — needs reconciling with the chosen title)
- Free to download; optional rewarded ads only (never forced); shop + ~1hr free-round refill timer
- **Publish as soon as ready — not waiting for a full portfolio**

**Crappy Turd** — second game, Flappy Bird-style, flying poop emoji, 16-frame sprite sheet + cover art done. No rush.

## Launch / marketing — firm rule
**No social posting and no ASO/store listing work until Rune Raid is fully tested, finalized, AND all supporting content is built.** This applies to both AI assistance and manual work — don't start the content pipeline early.

Reserved (not yet posted to): X, TikTok, Instagram, Reddit, Discord — handle `jaroflife`/`thejaroflife` (backup `runeraidgame`), tied to admin@thejaroflife.com. Skipping YouTube for now.

Site visibility plan (once live): Google Search Console submission, basic on-page SEO, itch.io/IndieDB listing, press kit outreach, relevant subreddits, Play Store ASO, dev blog posts.

## Full detail
See `jar-of-life-project-plan.pdf` (from Claude chat) for the complete version with reasoning/explanations — this file is the condensed working version.
