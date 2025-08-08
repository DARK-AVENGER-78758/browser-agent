import playwright.sync_api as sync

def automate_task():
    with sync.sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.linkedin.com')
        
        # Add more actions here if needed
        
        input("Press Enter to exit...")
        browser.close()

automate_task()