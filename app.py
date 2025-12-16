from flask import Flask, render_template, request
from fetcher import fetch_news

app = Flask(__name__)

@app.route("/")
def index():
    category = request.args.get("category", "general")
    articles = fetch_news(category)

    return render_template(
        "index.html",
        articles=articles,
        active_category=category
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
