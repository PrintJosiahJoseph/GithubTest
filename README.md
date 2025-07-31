# GithubTest

This repository contains a simple example of how to scrape apprenticeship listings from
`https://www.gov.uk/apply-apprenticeship` and filter the results so that only
Fortune 500 companies are shown. Network access to the URL may require
additional configuration depending on your environment.

## Setup

Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python scrape_apprenticeships.py
```

The script loads company names from `fortune500.txt` and prints any matches
found on the page. You can expand the list with the complete Fortune 500
companies as needed.
