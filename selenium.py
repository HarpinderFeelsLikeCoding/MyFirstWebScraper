from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the browser driver
driver = webdriver.Chrome()

try:
    # Open the GitHub repository page
    driver.get("https://github.com/HarpinderFeelsLikeCoding/MyFirstWebScraper")

    # Debug: Print the page title to ensure the page loads
    print(f"Page title: {driver.title}")

    # Locate and extract commit count
    try:
        commit = driver.find_element(By.CSS_SELECTOR, ".d-flex.flex-justify-between .Link--secondary").text
        print(f"Commit Count: {commit}")
    except Exception as e:
        print(f"Could not find commit count: {e}")

    # Locate and extract branches count
    try:
        branches = driver.find_element(By.XPATH, "//a[contains(@href, '/branches')]").text
        print(f"Branches: {branches}")
    except Exception as e:
        print(f"Could not find branches count: {e}")
finally:
    # Close the browser
    driver.quit()

