import feedparser
from datetime import datetime

# Define RSS feeds for each category
FEEDS = {
    "general": [
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://www.reutersagency.com/feed/?best-topics=general-news"
    ],
    "sports": [
        "https://www.espn.com/espn/rss/news",
        "https://www.skysports.com/rss/12040"
    ],
    "stocks": [
        "https://www.investing.com/rss/news.rss",
        "https://www.marketwatch.com/rss/topstories"
    ]
}

def fetch_news():
    articles = []
    for category, urls in FEEDS.items():
        for url in urls:
            feed = feedparser.parse(url)
            for entry in feed.entries[:10]:
                # Some feeds might not have summary or image
                summary = getattr(entry, "summary", "")
                image = getattr(entry, "media_content", [{"url": ""}])[0]["url"] if hasattr(entry, "media_content") else ""
                published = getattr(entry, "published", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                articles.append({
                    "title": entry.title,
                    "link": entry.link,
                    "summary": summary,
                    "image": image,
                    "category": category,
                    "published": published
                })
    return articles
