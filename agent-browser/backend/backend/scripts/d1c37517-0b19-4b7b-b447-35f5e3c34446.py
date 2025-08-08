import playwright.sync_api as sync

def automate_task():
    with sync.playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://vtop.vit.ac.in/")
        
        page.fill('input[name="uname"]', 'Anirudh2003')
        page.fill('input[name="passwd"]', 'King#78758')
        
        page.click('button[type="submit"]')
        
        input("Press Enter to exit...")

automate_task()