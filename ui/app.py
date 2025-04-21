# ui/app.py
import streamlit as st
import requests

st.set_page_config(page_title="News Sentiment Analyzer", layout="wide")

st.title("🗞️ News Summarization and Sentiment with Hindi Audio")

# Health check
try:
    health = requests.get("http://localhost:8000/")
    if health.status_code != 200:
        st.error("Backend is not running. Please start FastAPI.")
except:
    st.error("⚠️ Could not connect to the backend (http://localhost:8000). Make sure it's running.")

company = st.text_input("Enter a company name:")

if st.button("Analyze") and company:
    with st.spinner("Fetching and analyzing news..."):
        try:
            response = requests.get(f"http://localhost:8000/analyze?company={company}")
            response.raise_for_status()
            data = response.json()

            st.subheader(f"Results for {data['company']}")
            sentiments = {"Positive": 0, "Negative": 0, "Neutral": 0}
            for article in data['articles']:
                sentiments[article['sentiment']] += 1
                st.markdown(f"### [{article['title']}]({article['url']})")
                st.write(f"**Sentiment**: {article['sentiment']}")
                st.write(article['summary'])
                st.divider()

            st.subheader("🧠 Overall Sentiment Distribution")
            st.bar_chart(sentiments)

            st.subheader("🔈 Hindi TTS Output")
            all_summaries = ' '.join([a['summary'] for a in data['articles']])
            tts_res = requests.get(f"http://localhost:8000/tts?text={all_summaries}")
            if tts_res.status_code == 200:
                st.audio("output.mp3", format="audio/mp3")
            else:
                st.warning("Could not generate audio.")
        except Exception as e:
            st.error(f"Error during analysis: {e}")
