import playwright.sync_api as sync

def automate_task():
    with sync.sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.linkedin.com/login')
        page.fill('input[name="session_key"]', 'Anirudh')
        page.fill('input[name="session_password"]', 'A123')
        page.click('button[type="submit"]')
        input("Press Enter to exit...")

automate_task()