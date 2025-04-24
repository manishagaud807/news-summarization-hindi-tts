# README.md
"""
# News Summarization and Hindi TTS Application

## Description
A web app that fetches news articles related to a company, performs sentiment analysis, summarizes them, and reads the summary aloud in Hindi.

##  Features
- Scrape news from Bing
- Summarize articles using Transformers
- Analyze sentiment using VADER
- Generate Hindi speech with gTTS
- User-friendly UI with Streamlit

##  Setup
```bash
git clone <repo-url>
cd news-sentiment-tts
pip install -r requirements.txt
```

Run backend:
```bash
uvicorn app.main:app --reload
```

Run frontend:
```bash
streamlit run ui/app.py
```

##  Deployment
Deploy on Hugging Face Spaces using a standalone `Dockerfile` or as a Gradio/Streamlit Space.
"""
