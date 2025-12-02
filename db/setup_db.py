from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "qa_demo.db"
INIT_SQL = Path(__file__).parent / "init_db.sql"


def create_db():
    if DB_PATH.exists():
        DB_PATH.unlink()

    conn = sqlite3.connect(DB_PATH)
    try:
        with INIT_SQL.open("r", encoding="utf-8") as f:
            sql_script = f.read()
        conn.executescript(sql_script)
        conn.commit()
    finally:
        conn.close()


def main():
    create_db()


if __name__ == "__main__":
    main()
