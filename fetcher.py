import feedparser

RSS_FEEDS = {
    'World': 'http://feeds.bbci.co.uk/news/world/rss.xml',
    'Technology': 'http://feeds.bbci.co.uk/news/technology/rss.xml',
    'Sports': 'http://feeds.bbci.co.uk/sport/rss.xml',
    'Business': 'http://feeds.bbci.co.uk/news/business/rss.xml'
}

def fetch_news():
    articles = []
    for category, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:5]:  # get top 5 articles per category
            articles.append({
                'title': entry.title,
                'summary': entry.summary if 'summary' in entry else '',
                'link': entry.link,
                'image': entry.media_content[0]['url'] if 'media_content' in entry else '',
                'category': category
            })
    return articles
