import playwright.sync_api as sync

def automate_task():
    with sync.playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.youtube.com")
        print("Successfully opened YouTube")

if __name__ == "__main__":
    automate_task()