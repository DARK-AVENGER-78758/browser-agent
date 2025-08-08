import playwright.sync_api as sync

def automate_task():
    with sync.sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.youtube.com")
        page.type('input#search', 'Shanks VS Kid')
        page.press('input#search', 'Enter')
        input("Press Enter to exit...")

automate_task()