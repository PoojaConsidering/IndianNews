from fastapi import APIRouter
from backend.database import get_all_stats, get_latest_summary
from backend.models import DailyStat, SummaryResponse

router = APIRouter()

@router.get("/api/stats")
def get_stats():
    data = get_all_stats()
    return {"stats": data}

@router.get("/api/summary")
def get_summary():
    data = get_latest_summary()
    if not data:
        return {"error": "No data available yet"}
    return data