import feedparser

def fetch_news():
    feeds = {
        "technology": "https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml",
        "sports": "https://www.espn.com/espn/rss/news",  # Fixed sports feed
        "world": "https://rss.nytimes.com/services/xml/rss/nyt/World.xml",
        "stocks": "https://www.investing.com/rss/news.rss"  # New stocks feed
    }

    all_articles = []

    for category, url in feeds.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:  # limit 5 articles per category
            article = {
                "title": entry.title,
                "link": entry.link,
                "published": entry.published if 'published' in entry else '',
                "summary": entry.summary if 'summary' in entry else '',
                "image": entry.media_content[0]['url'] if 'media_content' in entry else "https://via.placeholder.com/400x200",
                "category": category
            }
            all_articles.append(article)

    return all_articles
