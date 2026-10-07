from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

HAPPY = [
    "love", "excit", "joy", "thrill", "best", "wonderful", "amazing", "grateful",
    "fantastic", "proud", "delight", "bless", "bliss", "ecstatic", "beautiful",
    "smiling", "celebrat", "overjoy", "dream come true", "perfect", "spectacular",
    "exceed", "energized", "alive", "cloud nine", "happiest", "happy", "fortunate",
    "grinning", "radiating", "happiness", "bursting", "hoping for", "surprise",
    "winning", "great", "awesome", "glad", "pleased", "brilliant", "superb",
    "excellent", "enjoy", "laugh", "cheer", "hooray",
]
SAD = [
    "worst", "lost", "heartbroken", "heartbreak", "fail", "terrible", "passed away",
    "reject", "devastat", "nobody", "regret", "layoff", "disappoint", "worse",
    "lonely", "abandon", "falling apart", "depress", "hopeless", "crying", "pain",
    "broken", "miserable", "exhaust", "traumat", "defeated", "sorrow", "empty",
    "anxiety", "grief", "worried", "shatter", "betray", "sadness", "haunted",
    "crushed", "burdened", "problems", "badly", "sad", "awful", "horrible", "hate",
    "upset", "unhappy", "tragic", "suffer", "died", "death", "cry", "tears",
    "gloomy", "helpless", "overwhelmed", "struggl",
]


def classify(text: str) -> str:
    t = text.lower()
    h = sum(1 for w in HAPPY if w in t)
    s = sum(1 for w in SAD if w in t)
    if "tears of joy" in t:
        h += 2
    if h > s:
        return "happy"
    if s > h:
        return "sad"
    return "neutral"


class Batch(BaseModel):
    sentences: List[str]


@app.post("/sentiment")
def sentiment(batch: Batch):
    return {"results": [{"sentence": s, "sentiment": classify(s)} for s in batch.sentences]}


@app.get("/")
def root():
    return {"status": "ok"}
