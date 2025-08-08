from playwright.sync_api import sync_playwright

def automate_task():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        page.goto("https://vtop.vit.ac.in/vtop/login")
        
        page.fill('input[name="uname"]', "Aniruddh2003")
        page.fill('input[name="passwd"]', "abhi")
        
        captcha_text = page.inner_text('label[for="captcha"]')
        captcha_result = eval(captcha_text.replace("=", ""))
        page.fill('input[name="captcha"]', str(captcha_result))
        
        page.click('button[type="submit"]')
        
        print("Successfully logged in to vtop!")
        
        browser.close()

if __name__ == "__main__":
    automate_task()