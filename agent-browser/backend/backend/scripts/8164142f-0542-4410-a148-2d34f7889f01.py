from playwright.sync_api from playwright.sync_api import sync_playwright

try:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        print("Browser opened", flush=True, flush=True)
        
        page.goto("https://www.youtube.com")
        print("Opened YouTube", flush=True, flush=True)
        
        page.wait_for_timeout(300000)  # Wait for 5 minutes (300,000 milliseconds)
        print("Waited for 5 minutes", flush=True, flush=True)
        
except Exception as e:
    print(f"An error occurred: {e}", flush=True)
    
input("Press Enter to exit...")