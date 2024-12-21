from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.accuweather.com/en/us/philadelphia/19102/weather-forecast/350540")
    
    temperature = page.text_content(".temperature")
    condition = page.text_content(".condition")
    
    print(f"Temperature: {temperature}")
    print(f"Condition: {condition}")
    browser.close()
#playwright doesnt' work as weel as i thought
# looks like there is another wbkit thing that is needed for playwrightto work on safari