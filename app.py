import os
from flask import Flask, render_template, request
from fetcher import fetch_news

app = Flask(__name__)

# ================================
# Routes
# ================================

@app.route("/")
def index():
    category = request.args.get("category", "top")
    news = fetch_news(category)
    return render_template(
        "index.html",
        news=news,
        category=category,
        site_name="A.I.O Global News"
    )

# Debug route to verify backend fetching
@app.route("/debug")
def debug():
    return fetch_news("top")

# HilltopAds verification file
@app.route("/f70d03fedff298bb7599.txt")
def hilltop_verify():
    return "f70d03fedff298bb7599"

# ================================
# Gunicorn / Render Entry
# ================================

# IMPORTANT:
# ❌ Do NOT add app.run()
# Gunicorn handles the server
