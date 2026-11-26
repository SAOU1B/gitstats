"""gitstats - print a short summary of a Git repository's history.

Usage: python gitstats.py [path-to-repo]
"""
import collections
import subprocess
import sys


def log_lines(repo):
    out = subprocess.run(["git", "-C", repo, "log", "--pretty=%an|%ad", "--date=short"],
                         capture_output=True, text=True, check=True).stdout
    return [line.split("|", 1) for line in out.splitlines() if line]


def summarize(entries):
    authors = collections.Counter(a for a, _ in entries)
    days = sorted({d for _, d in entries})
    return {"commits": len(entries), "authors": dict(authors),
            "first": days[0] if days else None, "last": days[-1] if days else None}


if __name__ == "__main__":
    s = summarize(log_lines(sys.argv[1] if len(sys.argv) > 1 else "."))
    print(f"Commits : {s['commits']}")
    print(f"Period  : {s['first']} -> {s['last']}")
    for name, n in s["authors"].items():
        print(f"Author  : {name} ({n} commits)")
