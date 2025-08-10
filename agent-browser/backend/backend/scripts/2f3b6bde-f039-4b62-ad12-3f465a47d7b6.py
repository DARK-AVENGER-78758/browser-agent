from playwright.sync_api import sync_playwright

def automate_task():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://www.linkedin.com')
        
        page.fill('input[name="session_key"]', 'abc')
        page.fill('input[name="session_password"]', 'abcd')
        
        page.click('button[type="submit"]')
        
        browser.close()
        
        print("LinkedIn login successful")

if __name__ == "__main__":
    automate_task()