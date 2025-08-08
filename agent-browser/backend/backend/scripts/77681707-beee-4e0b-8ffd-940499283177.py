import time
from playwright.sync_api import sync_playwright

def automate_task():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://vtop.vit.ac.in/student/")
        page.fill('input[name="uname"]', "Anirudh2003")
        page.fill('input[name="passwd"]', "A123")
        page.click('button[type="submit"]')
        
        input("Press Enter to exit...")

automate_task()