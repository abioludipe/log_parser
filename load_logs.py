import sqlite3
from pathlib import Path

def load_log(records, db_path="db/logs.db"):
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            level     TEXT,
            message   TEXT,
            timestamp TEXT,
            UNIQUE(timestamp, message)
        )
    """)
    cur.executemany(
        "INSERT OR IGNORE INTO logs (level, message, timestamp) VALUES (?, ?, ?)",
        ((r.get("level"), r.get("message"), r.get("timestamp")) for r in records)
    )
    con.commit()
    con.close()
