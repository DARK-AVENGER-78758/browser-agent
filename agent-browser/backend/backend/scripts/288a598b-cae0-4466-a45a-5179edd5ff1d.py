from playwright.sync_api import sync_playwright

def automate_task():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto('https://www.linkedin.com/login')
        page.fill('input[name="session_key"]', 'Aniruddh2003')
        page.fill('input[name="session_password"]', 'abhi')
        page.click('button[type="submit"]')
        
        page.wait_for_timeout(5000)
        
        browser.close()
        print("LinkedIn login successful")

if __name__ == "__main__":
    automate_task()