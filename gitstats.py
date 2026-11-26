"""gitstats - print a short summary of a Git repository's history.

Usage: python gitstats.py [--json] [path-to-repo]
"""
import collections
import json
import subprocess
import sys


class NotARepository(Exception):
    pass


def log_lines(repo):
    try:
        out = subprocess.run(["git", "-C", repo, "log", "--pretty=%an|%ad", "--date=short"],
                             capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        raise NotARepository(repo) from exc
    return [line.split("|", 1) for line in out.splitlines() if line]


def summarize(entries):
    authors = collections.Counter(a for a, _ in entries)
    days = sorted({d for _, d in entries})
    return {"commits": len(entries), "authors": dict(authors),
            "first": days[0] if days else None, "last": days[-1] if days else None}


def main(argv):
    as_json = "--json" in argv
    args = [a for a in argv if a != "--json"]
    repo = args[0] if args else "."
    try:
        s = summarize(log_lines(repo))
    except NotARepository:
        print(f"error: '{repo}' is not a Git repository", file=sys.stderr)
        return 1
    if as_json:
        print(json.dumps(s, ensure_ascii=False))
        return 0
    print(f"Commits : {s['commits']}")
    print(f"Period  : {s['first']} -> {s['last']}")
    for name, n in s["authors"].items():
        print(f"Author  : {name} ({n} commits)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
