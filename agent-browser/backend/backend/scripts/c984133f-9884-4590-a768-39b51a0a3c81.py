from playwright.sync_api import sync_playwright

def automate_task():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://vtop.vit.ac.in/")
        page.fill('input[name="uname"]', "Aniruddh2003")
        page.fill('input[name="passwd"]', "abhi")
        page.click('button[type="submit"]')
        
        print("Successfully logged in to VTOP!")

        browser.close()

if __name__ == "__main__":
    automate_task()