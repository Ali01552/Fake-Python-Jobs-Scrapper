"""Fake Python Jobs Scraper.

A web scraper that collects job listings from
https://realpython.github.io/fake-jobs/ and extracts, for every
listing:

* the job title
* the company name
* the location
* a link to the full job description ("Apply" link)

The listings are printed to the console and also saved to a CSV file
(default: jobs.csv in the current directory).

Requires the project's declared dependencies: requests, beautifulsoup4
(bs4) and lxml.

Usage:
    python App.py
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

JOBS_URL = "https://realpython.github.io/fake-jobs/"

# Where the scraped listings are saved as CSV.
OUTPUT_CSV = "jobs.csv"

# Chromium-like user agent so the target server treats us as a browser.
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/126.0.0.0 Safari/537.36"
    )
}


@dataclass(frozen=True)
class Job:
    """A single job listing scraped from the site."""

    title: str
    company: str
    location: str
    link: str

    def __repr__(self) -> str:
        return (
            f"Job(title={self.title!r}, company={self.company!r}, "
            f"location={self.location!r}, link={self.link!r})"
        )


def fetch_page(url: str = JOBS_URL) -> str:
    """Download the HTML of the given URL and return it as text.

    Raises ``requests.HTTPError`` if the server responds with an error
    status code.
    """
    response = requests.get(url, headers=HEADERS, timeout=10)
    response.raise_for_status()
    return response.text


def parse_jobs(html: str) -> list[Job]:
    """Parse job listings out of the page's HTML.

    Each listing lives inside a ``div.card`` element under
    ``#ResultsContainer`` on the page. The relevant pieces are:

    * title   -> ``h2.title``
    * company -> ``h3.company``
    * location-> ``p.location``
    * link    -> the "Apply" ``a.card-footer-item`` whose ``href``
                 points to the full description page (contains ``/jobs/``)

    Job cards without any of these fields are skipped so a partial or
    malformed card never breaks the whole run.
    """
    soup = BeautifulSoup(html, "lxml")
    jobs: list[Job] = []

    for card in soup.select("#ResultsContainer .card"):
        title = _text_of(card, "h2.title")
        company = _text_of(card, "h3.company")
        location = _text_of(card, "p.location")

        apply_link = card.select_one('a.card-footer-item[href*="/jobs/"]')
        link = urljoin(JOBS_URL, apply_link.get("href")) if apply_link else ""

        # A listing must have all four fields to be considered complete.
        if title and company and location and link:
            jobs.append(Job(title=title, company=company, location=location, link=link))

    return jobs


def _text_of(card, selector: str) -> str:
    """Return the normalized text of the first match, or an empty string."""
    node = card.select_one(selector)
    if node is None:
        return ""
    return " ".join(node.get_text(" ", strip=True).split())


def save_to_csv(jobs: list[Job], filename: str | Path = OUTPUT_CSV) -> None:
    """Export the scraped listings to a CSV file.

    The file is written with a UTF-8 BOM (``utf-8-sig``) so the headers
    render correctly when the CSV is opened in Excel, and with
    ``newline=""`` so the csv module controls line endings (no blank
    rows, even on Windows).
    """
    with open(filename, "w", newline="", encoding="utf-8-sig") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=["title", "company", "location", "link"],
        )
        writer.writeheader()
        for job in jobs:
            writer.writerow(
                {
                    "title": job.title,
                    "company": job.company,
                    "location": job.location,
                    "link": job.link,
                }
            )


def print_jobs(jobs: list[Job]) -> None:
    """Print the scraped listings in a readable format."""
    if not jobs:
        print("No job listings were found on the page.")
        return

    print(f"Found {len(jobs)} job listing(s):\n")
    for index, job in enumerate(jobs, start=1):
        print(f"{index}. {job.title}")
        print(f"   Company : {job.company}")
        print(f"   Location: {job.location}")
        print(f"   Apply   : {job.link}\n")


def main() -> None:
    """Scrape the fake jobs site, print the listings and save them CSV."""
    try:
        html = fetch_page()
        jobs = parse_jobs(html)
        print_jobs(jobs)
        save_to_csv(jobs)
        print(f"Saved {len(jobs)} listing(s) to {OUTPUT_CSV!r}.")
    except requests.RequestException as exc:
        print(f"Failed to fetch {JOBS_URL}: {exc}")
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
