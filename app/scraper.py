
# scraper.py
import requests
from bs4 import BeautifulSoup
from typing import List, Dict

def fetch_news_links(company_name: str, max_articles: int = 10) -> List[str]:
    search_url = f"https://www.bing.com/news/search?q={company_name}+company&FORM=HDRSC6"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = []
    for item in soup.select('a.title')[:max_articles]:
        link = item.get('href')
        if link and link.startswith('http'):
            links.append(link)

    return links

def extract_article_details(url: str) -> Dict[str, str]:
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')

        title = soup.title.string if soup.title else "No Title Found"
        paragraphs = soup.find_all('p')
        summary = ' '.join([p.get_text() for p in paragraphs[:3]])

        return {
            "url": url,
            "title": title.strip(),
            "summary": summary.strip()
        }
    except Exception as e:
        return {
            "url": url,
            "title": "Error fetching article",
            "summary": str(e)
        }

def get_news_articles(company_name: str) -> List[Dict[str, str]]:
    article_links = fetch_news_links(company_name)
    articles = []
    for url in article_links:
        articles.append(extract_article_details(url))
    return articles