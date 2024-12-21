from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
import time

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get('https://orteil.dashnet.org/cookieclicker/')

# IDs and prefixes
cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

# Wait for the language selection and click 'English'
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'English')]"))
)
language = driver.find_element(By.XPATH, "//*[contains(text(), 'English')]")
language.click()

# Wait for the cookie element to be present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, cookie_id))
)


while True:
    try:
        # Re-locate the cookie element in every iteration, casuing the issue earlier
        cookie = driver.find_element(By.ID, cookie_id)
        cookie.click()
        
        # Get the initial cookie count
        cookies_count = driver.find_element(By.ID, cookies_id).text.split(" ")[0]
        cookies_count = int(cookies_count.replace(",", ""))
        
        # Check and buy affordable items for boosting the cookies
        for i in range(4):
            try:
                product_price_elem = driver.find_element(By.ID, product_price_prefix + str(i))
                product_price = product_price_elem.text.replace(",", "")
                
                if not product_price.isdigit():
                    continue

                product_price = int(product_price)

                if cookies_count >= product_price:
                    product = driver.find_element(By.ID, product_prefix + str(i))
                    product.click()
                    break
            except Exception as e:
                print(f"Error with product {i}: {e}")
                continue
    except StaleElementReferenceException:
        print("Stale element detected. Re-locating the cookie.")
    except Exception as e:
        print(f"Unexpected error: {e}")
