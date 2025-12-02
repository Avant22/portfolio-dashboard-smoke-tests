from pathlib import Path
import sqlite3

import pytest

DB_PATH = Path(__file__).resolve().parents[2] / "db" / "qa_demo.db"


@pytest.mark.db
def test_user_email_present():
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.execute("SELECT email FROM users WHERE id = ?", ("2",))
        row = cursor.fetchone()
    finally:
        conn.close()

    assert row is not None, "Expected user with id '2' to exist"
    assert row[0] == "qa+portfolio@example.com"


@pytest.mark.db
def test_positions_exist_for_user():
    conn = sqlite3.connect(DB_PATH)
    try:
        cursor = conn.execute(
            "SELECT COUNT(*) FROM portfolio_positions WHERE user_id = ?", ("2",)
        )
        (count,) = cursor.fetchone()
    finally:
        conn.close()

    assert count > 0, "Expected at least one portfolio position for user '2'"
