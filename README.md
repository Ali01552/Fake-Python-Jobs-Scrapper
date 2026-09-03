# Fake Python Jobs Scraper

A small **Python web-scraping practice project** that collects job listings from the [Real Python Fake Jobs](https://realpython.github.io/fake-jobs/) website.

> **Note:** This project was created primarily for learning and practice. It is not intended to be a production-ready job scraping application. https://roadmap.sh/projects/job-listings-scraper

## 🎯 Project Purpose

The main purpose of this project is to practice the fundamentals of:

- Python web scraping
- HTTP requests
- HTML parsing
- CSS selectors
- Working with structured data
- Python `dataclasses`
- CSV file generation
- Basic error handling
- Organizing a small Python project

The target website is specifically designed as a fake job board for practicing web scraping, making it suitable for this type of training project.

## ✨ Features

The scraper extracts the following information from each job listing:

- **Job title**
- **Company name**
- **Location**
- **Job description URL**

The extracted listings are:

1. Printed to the terminal in a readable format.
2. Saved to a CSV file named `jobs.csv`.

## 🛠️ Technologies Used

- **Python**
- [`requests`](https://requests.readthedocs.io/) — downloading the webpage
- [`BeautifulSoup`](https://www.crummy.com/software/BeautifulSoup/) — parsing HTML
- **lxml** — HTML parser used by BeautifulSoup
- **csv** — exporting the results
- **dataclasses** — representing job listings as structured Python objects

## 📁 Project Structure

```text
Fake-Python-Jobs-Scrapper/
│
├── App.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
│
└── src/
    └── fake_python_jobs_scrapper/
        └── __init__.py
```

## 🔄 How It Works

The application follows a simple scraping pipeline:

```text
Fake Jobs Website
       │
       ▼
   HTTP Request
       │
       ▼
 Download HTML
       │
       ▼
 BeautifulSoup
       │
       ▼
 Find Job Cards
       │
       ▼
 Extract Job Data
       │
       ▼
    Job Objects
       │
       ├───────────────┐
       ▼               ▼
   Terminal          jobs.csv
```

### 1. Fetch the webpage

The application sends an HTTP GET request to:

```text
https://realpython.github.io/fake-jobs/
```

A browser-like User-Agent is included in the request.

### 2. Parse the HTML

BeautifulSoup parses the returned HTML using the `lxml` parser.

The scraper searches for job cards inside:

```text
#ResultsContainer .card
```

### 3. Extract the information

For each card, the scraper looks for:

```text
h2.title       → Job title
h3.company     → Company
p.location     → Location
Apply link     → Job description URL
```

Incomplete listings are ignored.

### 4. Store the data

Each complete listing is represented using a `Job` dataclass:

```python
Job(
    title=...,
    company=...,
    location=...,
    link=...
)
```

### 5. Export the results

The listings are saved to:

```text
jobs.csv
```

The CSV contains four columns:

```text
title,company,location,link
```

## 🚀 Installation

Clone the repository:

```bash
git clone git@github.com:Ali01552/Fake-Python-Jobs-Scrapper.git
```

Move into the project directory:

```bash
cd Fake-Python-Jobs-Scrapper
```

Install the project's dependencies using your preferred Python environment/package manager.

If you're using `uv`, the project dependencies can be installed with:

```bash
uv sync
```

## ▶️ Usage

Run the application with:

```bash
python App.py
```

Or, if you're using `uv`:

```bash
uv run python App.py
```

The program will fetch the available fake job listings, display them in the terminal, and create:

```text
jobs.csv
```

## 🖥️ Example Output

The terminal output will look similar to:

```text
Found 100 job listing(s):

1. Python Developer
   Company : Example Company
   Location: New York, NY
   Apply   : https://realpython.github.io/fake-jobs/jobs/...

2. Software Engineer
   Company : Example Company
   Location: Remote
   Apply   : https://realpython.github.io/fake-jobs/jobs/...

...

Saved 100 listing(s) to 'jobs.csv'.
```

*The exact listings and number of results may change depending on the current contents of the practice website.*

## 📊 CSV Output

The generated `jobs.csv` file contains:

| Column | Description |
|---|---|
| `title` | Job title |
| `company` | Company name |
| `location` | Job location |
| `link` | Link to the full job description |

The CSV is written using UTF-8 with BOM, which helps applications such as Microsoft Excel correctly recognize the encoding.

## 🧠 What I Learned

This project was built as a practical exercise to become more comfortable with Python and web scraping.

Key concepts practiced:

- Sending HTTP requests with `requests`
- Handling HTTP errors
- Parsing HTML with BeautifulSoup
- Using CSS selectors
- Extracting and cleaning text
- Working with URLs using `urljoin`
- Creating data models with `dataclass`
- Using type hints
- Reading and writing CSV files
- Basic exception handling
- Separating functionality into reusable functions
- Using Git and GitHub for version control

## ⚠️ Limitations

This is intentionally a **simple training project**.

It does not attempt to provide:

- A production-grade scraping architecture
- Database storage
- Scheduling
- Concurrent/asynchronous scraping
- Proxy rotation
- CAPTCHA handling
- Authentication
- Advanced anti-bot handling
- A graphical user interface
- A job-search API
- Real-world job aggregation

The target website is a **fake jobs website specifically intended for web-scraping practice**.

## 🔮 Possible Future Improvements

If I continue developing this project as a learning exercise, possible improvements include:

- Add command-line arguments
- Allow the user to specify the output filename
- Add pagination support
- Add filtering by location
- Add filtering by job title
- Add logging
- Add unit tests
- Improve project/package structure
- Add asynchronous requests
- Store results in SQLite
- Create a simple data-analysis notebook
- Generate statistics about the scraped jobs
- Add automated tests with `pytest`

## 📚 Project Context

This project is part of my journey toward becoming more comfortable with **Python, data analysis, automation, and web scraping**.

The goal is not to build a commercial scraper, but to learn by building something small and understandable from start to finish.

---

**Status:** 🟢 Training / Practice Project

**Language:** Python

**Purpose:** Learning & experimentation