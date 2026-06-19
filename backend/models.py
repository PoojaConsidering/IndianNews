from pydantic import BaseModel

class DailyStat(BaseModel):
    date: str
    india_count: int
    global_count: int

class SummaryResponse(BaseModel):
    date: str
    summary: str
    overview: str