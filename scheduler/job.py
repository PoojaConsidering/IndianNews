import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

from scraper.scraper import scrape_headlines
from scraper.classifier import classify_headlines
from summarizer.summarize import generate_summary
from backend.database import save_daily_data

def run_daily_job():
    print(f"\n[{datetime.now()}] Starting daily job...")

    # Step 1: Scrape
    headlines = scrape_headlines()
    print(f"Scraped {len(headlines)} headlines")

    # Step 2: Classify
    classified = classify_headlines(headlines)
    india_count = classified["india_count"]
    global_count = classified["global_count"]
    india_headlines = classified["india_headlines"]
    global_headlines = classified["global_headlines"]
    print(f"India: {india_count} | Global: {global_count}")

    # Step 3: Summarize
    summary_data = generate_summary(india_headlines, global_headlines)
    summary = summary_data["summary"]
    overview = summary_data["overview"]
    print("Summary generated")

    # Step 4: Save to database
    save_daily_data(
        date=datetime.now().strftime("%Y-%m-%d"),
        india_count=india_count,
        global_count=global_count,
        summary=summary,
        overview=overview
    )
    print("Data saved to database")
    print(f"[{datetime.now()}] Daily job complete.\n")


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(run_daily_job, "cron", hour=12, minute=0)
    print("Scheduler started. Waiting for 12:00 PM...")
    
    # Uncomment the line below to test immediately without waiting for 12 PM
    # run_daily_job()
    
    scheduler.start()