#!/usr/bin/env python3
"""Upload The Jar of Life website to Fasthosts over FTP(S).

Standard library only — no pip install needed.

Usage (from the project root):
    python scripts/deploy.py --dry-run   # list what would be uploaded, no connection
    python scripts/deploy.py             # upload for real

Reads FTP settings from .env in the project root (see .env.example).
Only the public site files below are uploaded; .env, README, scripts and
git files never leave your machine.
"""

import argparse
import ftplib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Public site files/folders. Anything not listed here is never uploaded.
PUBLISH = ["index.html", "games", "css", "assets"]

REQUIRED = ["FTP_HOST", "FTP_USER", "FTP_PASSWORD", "FTP_PORT"]
EXAMPLE_VALUES = {"your-ftp-username", "your-ftp-password"}


def load_env(path):
    """Minimal .env parser: KEY=VALUE lines, # comments, optional quotes."""
    if not path.exists():
        sys.exit(f"No .env found at {path}. Copy .env.example to .env and fill it in.")
    env = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        env[key.strip()] = value.strip().strip('"').strip("'")
    missing = [k for k in REQUIRED if not env.get(k)]
    if missing:
        sys.exit(f".env is missing: {', '.join(missing)}")
    if EXAMPLE_VALUES & {env["FTP_USER"], env["FTP_PASSWORD"]}:
        sys.exit(".env still has the example values — add the real Fasthosts credentials first.")
    return env


def collect_files():
    """Return (local_path, remote_relative_path) for every file to publish."""
    files = []
    for entry in PUBLISH:
        path = ROOT / entry
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(p for p in sorted(path.rglob("*")) if p.is_file())
    # Skip hidden files (.gitkeep, .DS_Store, etc.)
    files = [p for p in files if not any(part.startswith(".") for part in p.relative_to(ROOT).parts)]
    return [(p, p.relative_to(ROOT).as_posix()) for p in files]


def ensure_remote_dir(ftp, remote_dir, created):
    """Create remote_dir (relative to the current base) and its parents if needed."""
    parts = [p for p in remote_dir.split("/") if p]
    for i in range(1, len(parts) + 1):
        sub = "/".join(parts[:i])
        if sub in created:
            continue
        try:
            ftp.mkd(sub)
        except ftplib.error_perm:
            pass  # already exists
        created.add(sub)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="list files without connecting")
    args = parser.parse_args()

    files = collect_files()
    if not files:
        sys.exit("Nothing to upload.")

    if args.dry_run:
        print(f"Dry run — {len(files)} file(s) would be uploaded:")
        for _, remote in files:
            print(f"  {remote}")
        return

    env = load_env(ROOT / ".env")
    host = env["FTP_HOST"]
    port = int(env["FTP_PORT"])
    remote_base = env.get("FTP_REMOTE_DIR", "").strip("/")
    use_tls = env.get("FTP_TLS", "true").lower() != "false"

    ftp = ftplib.FTP_TLS() if use_tls else ftplib.FTP()
    print(f"Connecting to {host}:{port} ({'FTPS' if use_tls else 'plain FTP'})...")
    ftp.connect(host, port, timeout=30)
    ftp.login(env["FTP_USER"], env["FTP_PASSWORD"])
    if use_tls:
        ftp.prot_p()  # encrypt file transfers, not just the login

    try:
        if remote_base:
            ftp.cwd(remote_base)
        created = set()
        for local, remote in files:
            parent = remote.rsplit("/", 1)[0] if "/" in remote else ""
            if parent:
                ensure_remote_dir(ftp, parent, created)
            with open(local, "rb") as fh:
                ftp.storbinary(f"STOR {remote}", fh)
            print(f"  uploaded {remote}")
        print(f"Done — {len(files)} file(s) uploaded to {host}/{remote_base}")
    finally:
        try:
            ftp.quit()
        except ftplib.all_errors:
            ftp.close()


if __name__ == "__main__":
    main()
