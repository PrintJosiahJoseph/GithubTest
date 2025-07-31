import requests
from bs4 import BeautifulSoup
from typing import List, Dict

F500_FILE = 'fortune500.txt'
SEARCH_URL = 'https://www.gov.uk/apply-apprenticeship'


def load_fortune_500(filename: str = F500_FILE) -> List[str]:
    """Load Fortune 500 company names from a file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def scrape_apprenticeships(url: str, fortune_list: List[str]) -> List[Dict[str, str]]:
    """Fetch apprenticeship listings and filter for Fortune 500 companies."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    matches = []

    # Generic search: check all anchor tags for company names
    for anchor in soup.find_all('a'):
        text = anchor.get_text(' ', strip=True)
        for company in fortune_list:
            if company.lower() in text.lower():
                matches.append({
                    'company': company,
                    'title': text,
                    'url': anchor.get('href')
                })
                break
    return matches


def main():
    fortune_companies = load_fortune_500()
    try:
        results = scrape_apprenticeships(SEARCH_URL, fortune_companies)
    except Exception as exc:
        print(f"Error fetching data: {exc}")
        return

    if not results:
        print("No Fortune 500 companies found on the page.")
    else:
        for result in results:
            print(f"{result['company']}: {result['title']} -> {result['url']}")


if __name__ == '__main__':
    main()
