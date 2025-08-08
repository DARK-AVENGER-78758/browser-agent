import playwright.sync_api as sync

def automate_task():
    with sync.playwright.sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://vtop.vit.ac.in/vtop/login")
        page.fill('input[name="uname"]', 'Anirudh2003')
        page.fill('input[name="passwd"]', 'A123')
        page.click('text=Sign In')
        input("Press Enter to exit...")

automate_task()