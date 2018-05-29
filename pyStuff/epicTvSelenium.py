import os
import sys
import selenium
from selenium import webdriver

# Possibility to add Google Chrome extensions
from selenium.webdriver.chrome.options import Options

# Path for personal data
sys.path.append('/Volumes/StorEDGE/Alby/Python/Sensible_documents')

# Include personal data document
import Data

# Chromedriver path
chromedriver = "/usr/local/bin/chromedriver"

# Set chromedriver as environmental parameter
os.environ["webdriver.chrome.driver"] = chromedriver

# Set the webdriver adding the path and the options (extensions)
driver = webdriver.Chrome(executable_path=chromedriver)

# Get login page url
url = 'https://shop.epictv.it/it?'

driver.get(url)

# Find the login button on the page
logIn = driver.find_elements_by_css_selector("a")

logIn[9].click()
