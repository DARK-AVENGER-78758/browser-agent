from playwright.sync_api import sync_playwright

def automate_task():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://www.youtube.com")
        
        browser.close()
        print("Automation completed successfully.")

if __name__ == "__main__":
    automate_task()