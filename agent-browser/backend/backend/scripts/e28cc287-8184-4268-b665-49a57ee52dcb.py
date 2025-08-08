from playwright.sync_api from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    try:
        page.goto("https://vtop.vit.ac.in/vtop/login")
        print("Opened VTOP login page", flush=True, flush=True)

        page.fill('input[name="uname"]', "Anirudh2003")
        print("Filled username", flush=True, flush=True)

        page.fill('input[name="passwd"]', "A123")
        print("Filled password", flush=True, flush=True)

        page.click('button[type="submit"]')
        print("Clicked login button", flush=True, flush=True)

        page.wait_for_navigation()
        print("Logged in successfully", flush=True, flush=True)

    except Exception as e:
        print(f"An error occurred: {str(e, flush=True)}", flush=True)

    input("Press Enter to exit...")

    browser.close()