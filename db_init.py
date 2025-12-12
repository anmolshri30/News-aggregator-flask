import sqlite3

conn = sqlite3.connect('articles.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS articles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    link TEXT UNIQUE,
    summary TEXT,
    published TEXT,
    source TEXT,
    category TEXT,
    fetched_at TEXT
)
''')

conn.commit()
conn.close()
print('Database initialized: articles.db')
