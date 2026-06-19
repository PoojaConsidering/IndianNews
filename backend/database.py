import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "../database/news.db")

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_news (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT UNIQUE,
            india_count INTEGER,
            global_count INTEGER,
            summary TEXT,
            overview TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_daily_data(date, india_count, global_count, summary, overview):
    create_table()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO daily_news (date, india_count, global_count, summary, overview)
        VALUES (?, ?, ?, ?, ?)
    """, (date, india_count, global_count, summary, overview))
    conn.commit()
    conn.close()

def get_all_stats():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, india_count, global_count FROM daily_news ORDER BY date ASC")
    rows = cursor.fetchall()
    conn.close()
    return [{"date": r[0], "india_count": r[1], "global_count": r[2]} for r in rows]

def get_latest_summary():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, summary, overview FROM daily_news ORDER BY date DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"date": row[0], "summary": row[1], "overview": row[2]}
    return None