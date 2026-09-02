import os
import re
from playwright.sync_api import expect
from pages.login_page import LoginPage

BASE_URL = os.getenv("BASE_URL", "https://qa.workflowpro.com")

def test_user_login(page):
    email = os.getenv("TEST_USER_EMAIL")
    password = os.getenv("TEST_USER_PASSWORD")

    assert email, "TEST_USER_EMAIL is not configured"
    assert password, "TEST_USER_PASSWORD is not configured"

    page.goto(f"{BASE_URL}/login", wait_until="domcontentloaded")

    login = LoginPage(page)
    login.login(email, password)

    expect(page).to_have_url(re.compile(r".*/dashboard"))
    expect(page.locator(".welcome-message")).to_be_visible()
