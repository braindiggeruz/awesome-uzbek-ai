"""Bounded external HTTP availability audit; no quality or editorial claims.

Writes a timestamped JSON report. 404/410 are broken; other failures require
manual review (authentication, throttling, bot defenses or network problems).
External checking is deliberately separate from deterministic pull-request CI.
"""
import argparse
import concurrent.futures
import datetime
import ipaddress
import json
import re
import socket
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parent.parent


def public_url(url):
    parts = urlsplit(url)
    if parts.scheme not in ("http", "https") or not parts.hostname or parts.username or parts.password:
        raise ValueError("Only credential-free HTTP(S) URLs are allowed")
    if parts.port not in (None, 80, 443):
        raise ValueError("Nonstandard ports are not audited")
    addresses = socket.getaddrinfo(parts.hostname, parts.port or (443 if parts.scheme == "https" else 80))
    if not addresses or any(not ipaddress.ip_address(a[4][0]).is_global for a in addresses):
        raise ValueError("Non-public network destination rejected")
    return urlunsplit(parts._replace(fragment=""))


class PublicRedirects(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        public_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)


def check_url(url, timeout):
    result = {"url": url, "status": "review_required", "http_status": None}
    try:
        public_url(url)
        request = urllib.request.Request(url, headers={"User-Agent": "AwesomeUzbekAI-LinkAudit/1.0 (+https://github.com/braindiggeruz/awesome-uzbek-ai)", "Range": "bytes=0-1023"})
        opener = urllib.request.build_opener(PublicRedirects())
        with opener.open(request, timeout=timeout) as response:
            response.read(1024)
            result.update(http_status=response.status, final_url=response.url, status="reachable")
    except urllib.error.HTTPError as e:
        result.update(http_status=e.code, status="broken" if e.code in (404, 410) else "review_required", detail=str(e))
    except (OSError, ValueError, urllib.error.URLError) as e:
        result["detail"] = str(e)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", default="reports/link-check.json")
    parser.add_argument("--timeout", type=int, default=15)
    parser.add_argument("--workers", type=int, default=6)
    parser.add_argument("--limit", type=int, help="Audit only this many URLs; report explicitly records partial coverage")
    parser.add_argument("--fail-on-broken", action="store_true")
    args = parser.parse_args()
    paths = [ROOT / "README.md"] + sorted((ROOT / "guides").glob("*.md"))
    urls = sorted(set(url.split("#")[0] for p in paths for url in re.findall(r"\]\((https?://[^\s)]+)\)", p.read_text(encoding="utf-8"))))
    selected = urls[:args.limit] if args.limit is not None else urls
    started = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with concurrent.futures.ThreadPoolExecutor(max_workers=min(max(args.workers, 1), 8)) as pool:
        results = list(pool.map(lambda u: check_url(u, args.timeout), selected))
    summary = {status: sum(r["status"] == status for r in results) for status in ("reachable", "broken", "review_required")}
    report = {"started_at": started, "finished_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "method": "Public HTTP GET, up to 1024 response bytes; redirects checked. Does not assess content quality, ownership, language support, licensing or pricing.", "source_files": [p.relative_to(ROOT).as_posix() for p in paths], "total_discovered": len(urls), "total_checked": len(selected), "partial": len(selected) != len(urls), "summary": summary, "results": results}
    out = Path(args.output); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"report": str(out), **summary, "partial": report["partial"]}))
    if args.fail_on_broken and summary["broken"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
