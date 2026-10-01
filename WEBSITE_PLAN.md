# The Jar of Life — Website & Launch Context

Handoff notes from planning done in Claude chat. Read this at session start for context.

## Brand
- Domain: thejaroflife.com (registered, Fasthosts)
- Emails live: support@thejaroflife.com (public), admin@thejaroflife.com (accounts/registrations)
- Logo: made with Gemini, used in site repo already

## Hosting / DNS / SSL — current status
- Fasthosts web hosting is live; the coming-soon page is deployed (stage 1). FTP: host `ftp.fasthosts.co.uk`, user `thejaroflife.com`, `FTP_REMOTE_DIR` blank (login lands in htdocs). Fasthosts' old placeholder `_index.htm` was deleted from htdocs on 1 Oct 2026 (now 404)
- **In progress: migrating DNS + SSL to Cloudflare** (decided against Fasthosts' SSL add-on — free 1st year, ~£37.45/yr after; Cloudflare's is free permanently)
- Cloudflare account registered under admin@thejaroflife.com (Hotmail as recovery)
- Migration steps: Cloudflare account → add domain → verify DNS scan caught existing A + MX records → swap nameservers at Fasthosts → wait for propagation → re-test admin@/support@ email delivery
- Cloudflare SSL setting: choose **Flexible** (Fasthosts has no SSL certificate on the server, so "Full" would show a Cloudflare error). Turn on **Always Use HTTPS**. After the switch, check the site has the padlock and send test emails to support@ and admin@.

## Site content still needed (repo TODOs)
Done: studio logo + header icon, Runic Raid key art (portrait), story comic, social share images, 4 work-in-progress screenshots, privacy policy draft, `app-ads.txt` placeholder, `robots.txt` + `sitemap.xml`. Full checklist in `README.md`.

Still to do:
- Runic Raid cover art: landscape ~1600×1000 (optional — the site uses the portrait key art for now)
- Simpler purpose-made header/tab icon (optional — the current one is cropped from the studio logo)
- Final Runic Raid phone screenshots to replace the 4 work-in-progress ones
- Copy review: hero tagline, Runic Raid pitch, feature cards, fair play points, about text — all draft
- Privacy policy: set the date, confirm the age rating, update if analytics (e.g. Firebase) are added
- `app-ads.txt`: add the AdMob publisher ID
- Launch details: platforms, release date, store URLs

## Website rollout — 3 stages (agreed)
Publishing is done from Nicol's PC (`C:\CLAUDE_STUFF\thejaroflife-site`, FTP details in the local `.env`). See `CLAUDE.md` for the "Publish live website" rule.

1. **DONE 1 Oct 2026 — coming-soon page live at thejaroflife.com.** `python scripts/deploy.py --coming-soon` — studio logo, vague teaser (no game name), support email, privacy policy. Run from Nicol's PC (the cloud session can't reach Fasthosts). Fine to do before or after the Cloudflare switch.
2. **When Runic Raid is finalised and submitted to the Play Store: full site.** `python scripts/deploy.py` — homepage, Runic Raid page, full privacy policy. Before this: final screenshots, copy review, privacy policy check, AdMob ID in `app-ads.txt`.
3. **Once it's live on the Play Store: final tweak.** Add the real Google Play link/badge, swap "Coming soon" for "Available now", set the release date, then redeploy. Then the site visibility plan below (Search Console, etc.).

## Notes carried over from the setup chat (1 Oct 2026)
- **Email in Outlook (phone + laptop):** account type IMAP; username = full email address; Fasthosts servers (confirm in the control panel): incoming `imap.livemail.co.uk` port 993 SSL/TLS, outgoing `smtp.livemail.co.uk` port 465 SSL (or 587 STARTTLS), sign-in required.
- **Urgent-email monitoring:** plan in `docs/EMAIL_MONITORING.md` (daily, read-only, alerts only). Not set up yet — needs `support@` forwarded to Gmail/Outlook and that account connected to Claude.
- **Housekeeping:** the game repo still has an unused branch `claude/rename-runic-raid` (closed PR #1, never merged) — delete it on GitHub when convenient. Fasthosts' old `_index.htm` in htdocs can be deleted.
- **Repo visibility:** `NicolJarvie/first-pr-practice` is public. Optional: make it private (Settings → General → Danger Zone).
- **Stage 2 inputs needed:** final phone screenshots, copy review, Play Console age rating, analytics yes/no, AdMob publisher ID, Play Store URL and release date.

## Games
**Runic Raid: Viking Saga** — final name. Earlier working titles: "Rune Raiders" (dropped — naming conflict with an old Retro64 game), then "Rune Raid". Use "Runic Raid" everywhere.
- Reverse tower-defense: player controls Viking raiders, steals runes from defended strongholds
- Tap-to-send control scheme
- Playable build on device: level "1-3 Stone Bridge", squad tray, rune ability slots, gold counter, camera controls
- Prototype app icon exists, labelled "Runic Raid" (matches the final name)
- Free to download; optional rewarded ads only (never forced); shop + ~1hr free-round refill timer
- **Publish as soon as ready — not waiting for a full portfolio**

**Crappy Turd** — second game, Flappy Bird-style, flying poop emoji, 16-frame sprite sheet + cover art done. No rush.

## Launch / marketing — firm rule
**No social posting and no ASO/store listing work until Runic Raid is fully tested, finalized, AND all supporting content is built.** This applies to both AI assistance and manual work — don't start the content pipeline early.

Reserved (not yet posted to): X, TikTok, Instagram, Reddit, Discord — handle `jaroflife`/`thejaroflife` (backup `runeraidgame` — reserved under the old name; consider also reserving a `runicraid` handle), tied to admin@thejaroflife.com. Skipping YouTube for now.

Site visibility plan (once live): Google Search Console submission, basic on-page SEO, itch.io/IndieDB listing, press kit outreach, relevant subreddits, Play Store ASO, dev blog posts.

## Full detail
See `jar-of-life-project-plan.pdf` (from Claude chat) for the complete version with reasoning/explanations — this file is the condensed working version.
