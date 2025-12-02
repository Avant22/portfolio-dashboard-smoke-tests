import sys
from pathlib import Path

import pytest

# Ensure project root is on sys.path for test imports
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from db.setup_db import create_db


@pytest.fixture(scope="session", autouse=True)
def ensure_db_seeded():
    """
    Build/seed the SQLite DB before any DB tests run.
    """
    create_db()
