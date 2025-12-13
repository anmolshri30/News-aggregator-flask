from flask import Flask, render_template
from fetcher import fetch_news

app = Flask(__name__)

categories = ["technology", "sports", "world", "stocks"]

@app.route("/")
def home():
    articles = fetch_news()
    return render_template("index.html", articles=articles, categories=categories, active_category="All")

@app.route("/category/<category>")
def category_page(category):
    articles = [a for a in fetch_news() if a["category"] == category]
    return render_template("index.html", articles=articles, categories=categories, active_category=category)

if __name__ == "__main__":
    app.run(debug=True)
