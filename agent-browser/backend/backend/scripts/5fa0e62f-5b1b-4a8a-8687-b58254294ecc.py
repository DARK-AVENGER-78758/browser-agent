from playwright.sync_api import sync_playwright

def automate_task():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://www.instagram.com/accounts/login/')
        
        print("Successfully opened Instagram login page")
        
        browser.close()

if __name__ == "__main__":
    automate_task()