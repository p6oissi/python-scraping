import datetime
import json
import os
import time

from src.scrapers.arvutitark_scraper import scrape_arvutitark
from src.scrapers.yaga_scraper import scarpe_yaga

def search_all_sites(keyword):
    """
    Calls all scraper functions and combines their results.
    """
    results = []
    results.extend(scarpe_yaga(keyword))
    results.extend(scrape_arvutitark(keyword))
    return results

def run_periodically(keyword, interval=300):
    """
    Re-runs the search every 'interval' seconds.
    """
    seen_links = set()
    while True:
        results = search_all_sites(keyword)

        new_items = [result for result in results if result['link'] not in seen_links]
        for result in new_items:
            seen_links.add(result['link'])

        print("\n" + "=" * 60)
        print(f"Results for '{keyword}' ({len(new_items)} items found)")
        print(f"\nSearch run at {datetime.datetime.now().strftime('%H:%M:%S')}")
        print("=" * 60)
        if not new_items:
            print("No *new* results found.")
        else:
            for idx, item in enumerate(new_items, start=1):
                print(f"\nProduct #{idx}")
                print(f"Name: {item['name']}")
                print(f"Price: {item['price']}")
                print(f"Link: {item['link']}")
                print(f"Source: {item['site']}")
                print("-" * 60)

            print(f"\nWaiting {interval} seconds before next check...\n")
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H-%M-%S')
            filename = f"results-{keyword}_{timestamp}.json"
            os.makedirs("results", exist_ok=True)
            with open(os.path.join("results", filename), "w", encoding="utf-8") as f:
                json.dump(new_items, f, ensure_ascii=False, indent=2)
            time.sleep(interval)
