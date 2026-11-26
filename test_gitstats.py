import tempfile

from gitstats import main, summarize


def test_summarize():
    s = summarize([["A", "2026-11-26"], ["B", "2026-11-27"], ["A", "2026-11-28"]])
    assert s["commits"] == 3
    assert s["authors"] == {"A": 2, "B": 1}
    assert (s["first"], s["last"]) == ("2026-11-26", "2026-11-28")


def test_not_a_repository_returns_error_code():
    with tempfile.TemporaryDirectory() as empty_dir:
        assert main([empty_dir]) == 1


if __name__ == "__main__":
    test_summarize()
    test_not_a_repository_returns_error_code()
    print("ok")
