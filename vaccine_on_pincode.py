
""" 
Developer: aipython on [29-05-2021]
website: www.aipython.in

Sends Notifications on a Telegram channel , whenever the Vaccine(s) is available at the given PINCODE 
"""
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

# from os import environ

# Define all the constants
op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-sh-usage")
try:
    print('in try block')
    driver = webdriver.Chrome(service=Service(executable_path=os.environ.get("CHROMEDRIVER_PATH")), chrome_options=op)
except Exception as e:
	print("Exception arrived", e)
driver.get("https://venetablinds.com.au/")
print(driver.title)
driver.quit()
