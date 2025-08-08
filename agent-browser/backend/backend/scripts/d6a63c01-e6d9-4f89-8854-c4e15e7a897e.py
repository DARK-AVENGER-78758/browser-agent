import playwright.sync_api as sync

def automate_task():
    with sync.playwright.sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.youtube.com/")
        page.click("text=Sign in")
        page.fill('input[name="identifier"]', "Anirudh")
        page.click("text=Next")
        page.fill('input[name="password"]', "A123")
        page.click("text=Next")
        
        input("Press Enter to exit...")

automate_task()