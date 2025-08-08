import playwright.sync_api as sync

def automate_task():
    with sync.sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.youtube.com")
        page.wait_for_timeout(5000)
        input("Press Enter to exit...")

automate_task()