from flask import Flask, render_template, request
from fetcher import fetch_rss
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# Fully updated RSS feeds for all categories
RSS_FEEDS = {
    "All": [
        "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
        "https://feeds.bbci.co.uk/news/world/rss.xml",
    ],
    "Technology": [
        "https://www.theverge.com/rss/index.xml",
        "https://techcrunch.com/feed/",
        "https://www.wired.com/feed/rss",
    ],
    "Sports": [
        "https://www.espn.com/espn/rss/news",
        "https://feeds.bbci.co.uk/sport/rss.xml",
        "https://www.sportingnews.com/us/rss",
    ],
    "Business": [
        "https://www.cnbc.com/id/10001147/device/rss/rss.html",
        "https://feeds.marketwatch.com/marketwatch/topstories/",
        "https://www.reutersagency.com/feed/?best-topics=business-finance",
    ],
    "Entertainment": [
        "https://variety.com/feed/",
        "https://www.eonline.com/syndication/feeds/rssfeeds/topstories.xml",
        "https://www.hollywoodreporter.com/t/feed/entertainment",
    ],
    "Science": [
        "https://www.sciencedaily.com/rss/top/science.xml",
        "https://www.nasa.gov/rss/dyn/breaking_news.rss",
        "https://www.nature.com/subjects/science/rss.xml",
    ]
}

# Cached articles
cached_articles = []

def update_news():
    global cached_articles
    all_articles = []
    for category, urls in RSS_FEEDS.items():
        for feed in urls:
            articles = fetch_rss(feed)
            for a in articles:
                a['category'] = category  # assign category
            all_articles.extend(articles)
    cached_articles = sorted(all_articles, key=lambda x: x.get("pubDate", ""), reverse=True)
    print(f"News updated! Total articles: {len(cached_articles)}")

# Scheduler to update news every 10 minutes
scheduler = BackgroundScheduler()
scheduler.add_job(func=update_news, trigger="interval", minutes=10)
scheduler.start()

@app.route('/')
def home():
    category = request.args.get('category', 'All')
    if category == 'All':
        filtered_articles = cached_articles
    else:
        filtered_articles = [a for a in cached_articles if a.get('category') == category]
    return render_template("index.html", articles=filtered_articles)

if __name__ == "__main__":
    update_news()  # Initial fetch
    app.run(debug=True)

from flask import send_from_directory
import os

@app.route('/f70d03fedff298bb7599.txt')
def hilltopads_verify():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'f70d03fedff298bb7599.txt')
