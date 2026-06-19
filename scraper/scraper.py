import requests
from bs4 import BeautifulSoup
from scraper.sites import SITES

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"
}

def scrape_headlines():
    all_headlines = []

    for site in SITES:
        try:
            response = requests.get(site["url"], headers=HEADERS, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")
            tags = soup.select(site["headline_selector"])
            headlines = [tag.get_text(strip=True) for tag in tags if tag.get_text(strip=True)]
            print(f"[{site['name']}] Found {len(headlines)} headlines")
            all_headlines.extend(headlines)
        except Exception as e:
            print(f"[{site['name']}] Error: {e}")

    return all_headlines


if __name__ == "__main__":
    headlines = scrape_headlines()
    print(f"\nTotal headlines scraped: {len(headlines)}")
    for h in headlines[:10]:
        print(" -", h)