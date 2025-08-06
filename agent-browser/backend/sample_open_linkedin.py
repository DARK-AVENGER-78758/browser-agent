from dotenv import load_dotenv
import os
from playwright.sync_api import sync_playwright

# Load .env from current directory (backend/.env)
load_dotenv()

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.linkedin.com")
        print("LinkedIn opened successfully!")
        browser.close()

if __name__ == "__main__":
    run()
    print("API KEY:", os.getenv("OPENROUTER_API_KEY"))
