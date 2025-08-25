import requests
from bs4 import BeautifulSoup
from datetime import datetime

def fetch_news_headlines(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # raise exception for bad status codes
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website: {e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract headlines from <h3> or <h2> tags
    headlines = []
    for tag in soup.find_all(['h2', 'h3']):
        text = tag.get_text(strip=True)
        if text and len(text.split()) > 3:  # filter short/irrelevant ones
            headlines.append(text)

    return headlines

def save_to_txt(headlines, filename="headlines.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"News Headlines - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        for i, headline in enumerate(headlines, start=1):
            file.write(f"{i}. {headline}\n")

if __name__ == "__main__":
    url = "https://www.bbc.com/news"
    print(f"Fetching news from {url}...\n")
    headlines = fetch_news_headlines(url)

    if headlines:
        save_to_txt(headlines)
        print(f"✅ {len(headlines)} headlines saved to 'headlines.txt'")
    else:
        print("⚠️ No headlines found or an error occurred.")
