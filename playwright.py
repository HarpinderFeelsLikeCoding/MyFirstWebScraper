from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://github.com/HarpinderFeelsLikeCoding/MyFirstWebScraper")
    
    temperature = page.text_content(".temperature")
    condition = page.text_content(".condition")
    
    print(f"Temperature: {temperature}")
    print(f"Condition: {condition}")
    browser.close()
#playwright doesnt' work as weel as i thought