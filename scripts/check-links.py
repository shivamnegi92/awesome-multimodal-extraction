#!/usr/bin/env python3
"""Verify every link in README.md is alive. CI fails on dead links.

A list that promises 'no dead links' has to prove it. This is the receipt.
"""
import re
import sys
import urllib.request
import urllib.error

README = "README.md"
LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")

# Hosts that block HEAD/bots but are known-good infra; treat non-error as OK.
SKIP = ("awesome.re", "licensebuttons.net", "creativecommons.org")

UA = "awesome-entity-extraction-linkcheck/1.0 (+https://github.com)"


def check(url: str) -> tuple[bool, str]:
    if any(s in url for s in SKIP):
        return True, "skipped (known infra)"
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return (r.status < 400, str(r.status))
    except urllib.error.HTTPError as e:
        # Some hosts reject HEAD; retry with GET before failing.
        if e.code in (403, 405, 501):
            try:
                req2 = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req2, timeout=15) as r2:
                    return (r2.status < 400, str(r2.status))
            except Exception as e2:  # noqa: BLE001
                return False, f"{e.code} then {e2}"
        return False, str(e.code)
    except Exception as e:  # noqa: BLE001
        return False, str(e)


def main() -> int:
    with open(README, encoding="utf-8") as f:
        urls = sorted(set(LINK_RE.findall(f.read())))
    print(f"checking {len(urls)} links...\n")
    failures = []
    for u in urls:
        ok, info = check(u)
        print(f"  {'OK ' if ok else 'BAD'}  {info:>22}  {u}")
        if not ok:
            failures.append((u, info))
    print()
    if failures:
        print(f"{len(failures)} dead link(s):")
        for u, info in failures:
            print(f"  - {u} ({info})")
        return 1
    print(f"all {len(urls)} links alive.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
