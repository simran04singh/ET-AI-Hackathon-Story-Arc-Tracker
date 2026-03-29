from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="ET Story Arc Tracker API")

# Data Models based on Architecture Document
class StoryNode(BaseModel):
    date: str
    event: str
    source: str
    impact_score: float

class ArcResponse(BaseModel):
    topic: str
    timeline: List[StoryNode]
    sentiment_score: float
    contrarian_view: str
    next_steps: List[str]

# Mock Database for Hackathon Demo
mock_db = {
    "ev_market": {
        "topic": "Electric Vehicle Infrastructure India",
        "timeline": [
            {"date": "2025-10-12", "event": "FAME III Policy Draft Leaked", "source": "ET Bureau", "impact_score": 0.8},
            {"date": "2026-01-05", "event": "Major JV for Battery Swapping", "source": "MCA Filings", "impact_score": 0.9}
        ],
        "sentiment_score": 0.75,
        "contrarian_view": "While consensus is bullish on charging stations, regulatory delays in grid upgrades may stall growth.",
        "next_steps": ["Watch for PLI disbursement news", "Monitor BIS certification updates"]
    }
}

@app.get("/")
def home():
    return {"status": "Story Arc Tracker is Online", "problem_statement": "PS 8: AI-Native News"}

@app.get("/tracker/{topic}", response_model=ArcResponse)
def get_story_arc(topic: str):
    if topic not in mock_db:
        raise HTTPException(status_code=404, detail="Story arc not found")
    return mock_db[topic]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)