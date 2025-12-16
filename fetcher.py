import feedparser

FEEDS = {
    "general": [
        "https://rss.cnn.com/rss/edition.rss",
        "https://feeds.bbci.co.uk/news/rss.xml"
    ],
    "business": [
        "https://feeds.bbci.co.uk/news/business/rss.xml",
        "https://www.cnbc.com/id/10001147/device/rss/rss.html"
    ],
    "technology": [
        "https://feeds.arstechnica.com/arstechnica/index",
        "https://www.theverge.com/rss/index.xml"
    ],
    "sports": [
        "https://www.espn.com/espn/rss/news",
        "https://feeds.bbci.co.uk/sport/rss.xml"
    ],
    "entertainment": [
        "https://feeds.bbci.co.uk/news/entertainment_and_arts/rss.xml"
    ],
    "science": [
        "https://feeds.bbci.co.uk/news/science_and_environment/rss.xml"
    ],
    "stocks": [
        "https://www.cnbc.com/id/15839135/device/rss/rss.html",
        "https://feeds.marketwatch.com/marketwatch/topstories/"
    ]
}

DEFAULT_IMAGE = "https://via.placeholder.com/400x200?text=News"

def extract_image(entry):
    if "media_content" in entry:
        return entry.media_content[0].get("url", DEFAULT_IMAGE)
    if "media_thumbnail" in entry:
        return entry.media_thumbnail[0].get("url", DEFAULT_IMAGE)
    return DEFAULT_IMAGE

def fetch_news(category):
    articles = []

    for feed_url in FEEDS.get(category, []):
        feed = feedparser.parse(feed_url)

        for entry in feed.entries[:10]:
            articles.append({
                "title": entry.get("title", "No title"),
                "link": entry.get("link", "#"),
                "summary": entry.get("summary", ""),
                "image": extract_image(entry),
                "source": feed.feed.get("title", "Unknown")
            })

    return articles
