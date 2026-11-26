# gitstats

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**gitstats** is a tiny command-line tool that summarises the commit history of a Git repository:
how many commits it has, the period they cover, and how many commits each author made.
It was written as the demo project of my HBUT graduation internship on Git and GitHub, and it is
developed with the GitHub flow (issues → branches → pull requests → merge).

## Table of contents

- [Installation](#installation)
- [Usage](#usage)
- [Running the tests](#running-the-tests)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)

## Installation

gitstats only needs **Python 3.8+** and **Git** on your `PATH`.

```bash
git clone https://github.com/SAOU1B/gitstats.git
cd gitstats
```

## Usage

```bash
python gitstats.py [--json] [path-to-repository]
```

Example (plain text):

```text
$ python gitstats.py ../git-practice-project
Commits : 15
Period  : 2026-11-26 -> 2026-11-26
Author  : SAOUAB ZAKARIAE (15 commits)
```

Example (JSON, useful for other scripts):

```bash
python gitstats.py --json .
```

If the folder is not a Git repository, gitstats prints a short error and exits with status `1`.

## Running the tests

```bash
python test_gitstats.py
```

## Contributing

1. Open an [issue](https://github.com/SAOU1B/gitstats/issues) describing the bug or idea.
2. Create a branch with a descriptive name, e.g. `fix-not-a-repo`.
3. Commit small, well-described changes and open a pull request that references the issue (`Closes #N`).

See [docs/MARKDOWN_GUIDE.md](docs/MARKDOWN_GUIDE.md) for the Markdown conventions used in this repository.

## Credits

- Author: SAOUAB ZAKARIAE — Computer Science and Technology, Hubei University of Technology
- Based on the exercises of *Pro Git* (Scott Chacon and Ben Straub) and the GitHub Guides.

## Citation

If you use this software, please cite it using the metadata in [CITATION.cff](CITATION.cff).

## License

Released under the [MIT License](LICENSE).
