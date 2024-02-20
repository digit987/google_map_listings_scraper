import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_listing_details(listing_url):
    # Open Google Maps listing page
    driver.get(listing_url)

    # Wait for the page to load
    time.sleep(5)

    # Get company name
    company_name = driver.find_element(By.XPATH, "//h1").text
    print("Company Name:", company_name)

    # Locate and click on the copy button for website
    copy_button_company_website = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".RcCsl:nth-child(6) .g88MCb .EgL07d")))
    copy_button_company_website.click()

    # Retrieve copied text from clipboard for website
    company_website = pyperclip.paste()
    print("Company Website:", company_website)

    # Locate and click on the copy button for phone number
    copy_button_company_phone_number = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".RcCsl:nth-child(7) .g88MCb .EgL07d")))
    copy_button_company_phone_number.click()

    # Retrieve copied text from clipboard for phone number
    company_phone_number = pyperclip.paste()
    print("Company Phone Number:", company_phone_number)

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the URL
url = 'https://www.google.com/maps/search/it+companies+in+noida'
driver.get(url)

links=[]
# Find initial links
links.extend(driver.find_elements(By.CLASS_NAME, 'hfpxzc'))
'''
# Scrolling part cuurently not working. It just adds same same links 10 times in loop rather than 10 times different links in total
for i in range(10):  # Adjust the number of scrolls as needed
    # Scroll down
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)  # Adjust sleep time as needed
    links.extend(driver.find_elements(By.CLASS_NAME, 'hfpxzc'))
'''


listings_url_list = []

# Extract and open each link
for link in links:
    listing_url = link.get_attribute('href')
    print("Opening link:", listing_url)
    listings_url_list.append(listing_url)

print("Total crawled listings", len(listings_url_list))

print("Details of each listing are as follows")

for listing_url in listings_url_list:
    get_listing_details(listing_url)

# Close the browser
driver.quit()
