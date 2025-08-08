from playwright.sync_api from playwright.sync_api import sync_playwright

def automate_task():
    with sync_playwright() as p:
        print("Launching browser...", flush=True, flush=True)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("Navigating to https://vtop.vit.ac.in/vtop/login...", flush=True, flush=True)
        page.goto("https://vtop.vit.ac.in/vtop/login")
        
        print("Logging in with credentials...", flush=True, flush=True)
        page.fill('input[name="uname"]', 'Anirudh2003')
        page.fill('input[name="passwd"]', 'A123')
        page.click('input[type="submit"]')
        
        input("Press Enter to exit...")
        
try:
    automate_task()
except Exception as e:
    print(f"An error occurred: {str(e, flush=True)}")
    input("Press Enter to exit...")