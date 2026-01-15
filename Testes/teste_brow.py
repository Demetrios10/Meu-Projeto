import playwright
from playwright.sync_api import Page, expect

def test_(page: Page):
    page.goto("https://www.nike.com.br//")
    page.waitForTimeout(10000);

