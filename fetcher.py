import requests
import xml.etree.ElementTree as ET

def fetch_rss(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to fetch {url}, status: {response.status_code}")
            return []

        root = ET.fromstring(response.content)
        items = []
        for item in root.findall('.//item'):
            title = item.find('title').text if item.find('title') is not None else "No Title"
            link = item.find('link').text if item.find('link') is not None else "#"
            pub = item.find('pubDate').text if item.find('pubDate') is not None else ""
            desc = item.find('description').text if item.find('description') is not None else ""
            items.append({
                "title": title,
                "link": link,
                "pubDate": pub,
                "description": desc
            })
        print(f"Fetched {len(items)} articles from {url}")
        return items
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return []
