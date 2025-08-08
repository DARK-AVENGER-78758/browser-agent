import playwright.sync_api as sync

def automate_task():
    print("Launching browser...")
    browser = sync.chromium.launch(headless=False)
    page = browser.new_page()
    
    print("Navigating to https://vtop.vit.ac.in/vtop/login...")
    page.goto("https://vtop.vit.ac.in/vtop/login")
    
    print("Logging in with credentials...")
    page.fill('input[name="uname"]', 'Anirudh2003')
    page.fill('input[name="passwd"]', 'A123')
    page.click('input[type="submit"]')
    
    input("Press Enter to exit...")

automate_task()