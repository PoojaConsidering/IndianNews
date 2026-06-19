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

| Layer | Tool |
|---|---|
| Scraping | Python, BeautifulSoup, Requests |
| AI Classification & Summary | Claude API (Anthropic) |
| Scheduling | APScheduler |
| Backend API | FastAPI |
| Database | SQLite |
| Frontend | HTML, CSS, JavaScript, Chart.js |

---

## Project Structure

```
indian-news-tracker/
├── scraper/
│   ├── __init__.py
│   ├── sites.py
│   ├── scraper.py
│   └── classifier.py
├── summarizer/
│   ├── __init__.py
│   └── summarize.py
├── scheduler/
│   ├── __init__.py
│   └── job.py
├── backend/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── database.py
│   └── models.py
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── app.js
├── database/
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the repository
```
git clone https://github.com/your-username/indian-news-tracker.git
cd indian-news-tracker
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

### 3. Add your API key
Create a `.env` file in the root folder:
```
ANTHROPIC_API_KEY=your_api_key_here
```

### 4. Run the backend
```
uvicorn backend.main:app --reload
```

### 5. Start the scheduler
```
python scheduler/job.py
```

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