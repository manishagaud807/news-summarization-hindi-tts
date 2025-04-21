# app/main.py
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from app.scraper import get_news_articles
from app.summarizer import summarize_text
from app.sentiment import get_sentiment
from app.tts import generate_hindi_tts

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "FastAPI backend is running"}

@app.get("/analyze")
def analyze(company: str = Query(..., description="Company name for news analysis")):
    articles = get_news_articles(company)
    for article in articles:
        article['sentiment'] = get_sentiment(article['summary'])
        article['summary'] = summarize_text(article['summary'])
    return {"company": company, "articles": articles}

@app.get("/tts")
def text_to_speech(text: str):
    filename = generate_hindi_tts(text)
    return {"audio_file": filename}
