from playwright.sync_api from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        print("Opening YouTube...", flush=True)
        page.goto("https://www.youtube.com", wait_until="domcontentloaded")
        print("YouTube opened successfully.", flush=True)

        input("Press Enter to exit...")
    except Exception as e:
        print(f"An error occurred: {str(e, flush=True)}")

    browser.close()