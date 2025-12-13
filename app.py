from flask import Flask, render_template
from apscheduler.schedulers.background import BackgroundScheduler
from fetcher import fetch_news
import sqlite3
import atexit

app = Flask(__name__)
DB = "articles.db"

def init_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS articles
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  link TEXT,
                  summary TEXT,
                  image TEXT,
                  category TEXT,
                  published TEXT)''')
    conn.commit()
    conn.close()

init_db()

def update_articles():
    articles = fetch_news()
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    c.execute("DELETE FROM articles")
    for a in articles:
        c.execute("INSERT INTO articles (title, link, summary, image, category, published) VALUES (?, ?, ?, ?, ?, ?)",
                  (a["title"], a["link"], a["summary"], a["image"], a["category"], a["published"]))
    conn.commit()
    conn.close()
    print("Articles updated.")

scheduler = BackgroundScheduler()
scheduler.add_job(update_articles, 'interval', minutes=10)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())

@app.route("/")
@app.route("/category/<category>")
def index(category=None):
    conn = sqlite3.connect(DB)
    c = conn.cursor()
    if category:
        c.execute("SELECT * FROM articles WHERE category=? ORDER BY published DESC", (category,))
    else:
        c.execute("SELECT * FROM articles ORDER BY published DESC")
    articles = c.fetchall()
    conn.close()
    return render_template("index.html", articles=articles, category=category)

if __name__ == "__main__":
    update_articles()
    app.run(host="0.0.0.0", port=5000)
