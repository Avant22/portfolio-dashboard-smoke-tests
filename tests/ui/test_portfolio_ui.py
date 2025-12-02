from playwright.sync_api import sync_playwright
import pytest

import config


@pytest.mark.ui
def test_portfolio_login_and_inventory():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(config.UI_BASE_URL)
        page.fill("input[data-test='username']", config.TEST_USER_EMAIL)
        page.fill("input[data-test='password']", config.TEST_USER_PASSWORD)
        page.click("input[data-test='login-button']")

        page.wait_for_selector("div.inventory_list")
        items = page.query_selector_all("div.inventory_item")

        assert len(items) > 0, "Expected at least one inventory item after login"

        browser.close()
