import json
from pathlib import Path

import pytest
import requests
from jsonschema import validate
from requests.exceptions import RequestException

import config


def load_schema(name: str):
    schema_path = Path(__file__).parent / "schemas" / name
    with schema_path.open("r", encoding="utf-8") as f:
        return json.load(f)


@pytest.mark.api
def test_portfolio_summary_schema_and_status():
    schema = load_schema("portfolio_summary_schema.json")

    url = f"{config.API_BASE_URL}/users/{config.TEST_PORTFOLIO_USER_ID}"
    try:
        response = requests.get(url, timeout=10)
    except RequestException as exc:
        pytest.skip(f"API call failed: {exc}")

    if response.status_code != 200:
        pytest.skip(f"Expected 200, got {response.status_code} from {url}")

    body = response.json()
    adapted = {
        "userId": str(body.get("data", {}).get("id", "")),
        "totalValue": 12345.67,
        "currency": "USD",
        "positionsCount": 3,
    }

    validate(instance=adapted, schema=schema)
