import time
from playwright.sync_api import sync_playwright

def automate_task():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.youtube.com")
        time.sleep(10)
        input("Press Enter to exit...")
        browser.close()

automate_task()