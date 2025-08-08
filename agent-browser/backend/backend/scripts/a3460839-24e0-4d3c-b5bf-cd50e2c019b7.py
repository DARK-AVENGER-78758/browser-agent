import playwright.sync_api as sync

def automate_task():
    with sync.sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.youtube.com")
        
        input("Press Enter to exit...")
        browser.close()

automate_task()