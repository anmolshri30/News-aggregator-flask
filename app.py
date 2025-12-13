from flask import Flask, render_template
from fetcher import fetch_news

app = Flask(__name__)

@app.route('/')
def home():
    news = fetch_news()  # fetch all news
    return render_template('index.html', news=news)

@app.route('/category/<category_name>')
def category(category_name):
    all_news = fetch_news()
    category_news = [article for article in all_news if article['category'].lower() == category_name.lower()]
    return render_template('index.html', news=category_news)

if __name__ == '__main__':
    app.run(debug=True)
