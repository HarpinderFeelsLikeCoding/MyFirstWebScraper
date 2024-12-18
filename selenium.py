from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the browser driver
driver = webdriver.Chrome()

# Open the website
driver.get("https://github.com/HarpinderFeelsLikeCoding/MyFirstWebScraper")

# Wait for content to load and extract data
commit = driver.find_element(By.CLASS_NAME, "commit").text
branches = driver.find_element(By.CLASS_NAME, "branches").text

print(f"Temperature: {commit}")
print(f"Condition: {branches}")

# Close the browser
driver.quit()
