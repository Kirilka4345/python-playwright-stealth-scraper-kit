# Playwright Browser Automation Starter

A synchronous Playwright example with a persistent Chromium profile.

**Status: development starter / prototype.** Read the scope before integrating.

## Included

- Opens a page and returns its title and HTML character count.
- Includes optional browser initialization patches and a small unit suite.

## Scope and limitations

- No proxy rotation, JSON/CSV export pipeline or guaranteed anti-bot bypass.
- config.example.json is a reference; runtime settings live in CONFIG in stealth_scraper.py.
- Browser patches are experimental. Use only on websites you are authorized to automate.

## Quick start

Python 3.10+; run from the repository directory.

```sh
python -m pip install -r requirements.txt
python -m playwright install chromium
python stealth_scraper.py
```

## Validation

```sh
python -m unittest discover -s tests -v
```

The original unit checks cover configuration and patch strings; they do not validate website compatibility.

## Repository map

- `stealth_scraper.py` — implementation.
- `tests/` — current checks and regression tests.
- [CHANGELOG.md](CHANGELOG.md) — changes and verification limits.
- [CONTRIBUTING.md](CONTRIBUTING.md) — issue and change guidelines.

## Downloads and usage terms

[Repository releases](https://github.com/Kirilka4345/python-playwright-stealth-scraper-kit/releases) contain historical snapshots; use the current source for the documented fixes.
No LICENSE file is present. Earlier MIT badges and commercial-license claims did not establish usable license terms. License terms require clarification before redistribution.

## Questions

For reproducible technical issues, use [GitHub Issues](https://github.com/Kirilka4345/python-playwright-stealth-scraper-kit/issues). Include the commit, runtime version, expected result and minimal reproduction. Never include tokens, cookies or customer data.
