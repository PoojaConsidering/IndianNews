# Indian News Tracker

A full-stack web app that tracks how much of Indian news website coverage is India-focused vs global. It scrapes headlines daily, classifies them using AI, and displays the results as a graph with a summary.

---

## What It Does

- Scrapes headlines daily at 12:00 PM from major Indian news websites
- Uses Claude AI to classify each headline as India-focused or Global
- Generates a daily summary and detailed overview of Indian news
- Displays a graph of India vs Global news count over time
- Shows the latest AI-generated summary on the frontend

---

## Tech Stack

|
 Layer 
|
 Tool 
|
|
---
|
---
|
|
 Scraping 
|
 Python, BeautifulSoup, Requests 
|
|
 AI Classification & Summary 
|
 Claude API (Anthropic) 
|
|
 Scheduling 
|
 APScheduler 
|
|
 Backend API 
|
 FastAPI 
|
|
 Database 
|
 SQLite 
|
|
 Frontend 
|
 HTML, CSS, JavaScript, Chart.js 
|

---

## Project Structure
indian-news-tracker/
├── scraper/
│ ├── init.py
│ ├── sites.py # Target news websites and CSS selectors
│ ├── scraper.py # Fetches and parses headlines
│ └── classifier.py # Classifies headlines using Claude AI
├── summarizer/
│ ├── init.py
│ └── summarize.py # Generates summary and overview using Claude AI
├── scheduler/
│ ├── init.py
│ └── job.py # Runs the daily pipeline at 12:00 PM
├── backend/
│ ├── init.py
│ ├── main.py # FastAPI app
│ ├── routes.py # API endpoints
│ ├── database.py # SQLite operations
│ └── models.py # Pydantic models
├── frontend/
│ ├── index.html
│ ├── style.css
│ └── app.js
├── database/
│ └── news.db # Auto-created on first run
├── .env # API keys (never push this)
├── .gitignore
├── requirements.txt
└── README.md



---

## Setup Instructions

### 1. Clone the repository
git clone https://github.com/your-username/indian-news-tracker.git
cd indian-news-tracker



### 2. Install dependencies
pip install -r requirements.txt



### 3. Add your API key
Create a `.env` file in the root folder:
ANTHROPIC_API_KEY=your_api_key_here



### 4. Run the backend
uvicorn backend.main:app --reload



### 5. Start the scheduler
python scheduler/job.py



### 6. Open the frontend
Open `frontend/index.html` in your browser.

---

## API Endpoints

| Endpoint | Description |
|---|---|
| `GET /api/stats` | Returns India vs Global count for all dates |
| `GET /api/summary` | Returns the latest AI-generated summary and overview |

---

## Environment Variables

| Variable | Description |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic Claude API key |

---

## Notes

- The `database/news.db` file is auto-created on first run
- CSS selectors in `scraper/sites.py` may need updating if news websites change their HTML
- To test the pipeline immediately without waiting for 12 PM, uncomment `run_daily_job()` in `scheduler/job.py`