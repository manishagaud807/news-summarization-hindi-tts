# summarizer.py
from transformers import pipeline

summarizer = pipeline("summarization")

def summarize_text(text: str) -> str:
    if not text.strip():
        return "No content to summarize."
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']