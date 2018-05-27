# Script to take the free book from packtPub with selenium
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

# Set the possibility to add a chrome extension
chrome_options = Options()

#Add the captchaClicker extension. Before do that, it is important to download the
#extensions. To do so, paste the link on this site https://chrome-extension-downloader.com/ and download the
#crx file
chrome_options.add_extension('captchaClicker.crx')

# Set the webdriver adding the path and the options (extensions)
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)

# Open the browser and navigate to packtPub page
driver.get("https://www.packtpub.com/packt/offers/free-learning")

try:

    # Find the login button on the page
    logInPackt = driver.find_element_by_link_text("Log in")

# if nothing is found the NoSuchElementException is raised
except selenium.common.exceptions.NoSuchElementException:
    print("User already logged in")

    # Stop the program execution
    sys.exit()

# Click the login button
logInPackt.click()

# Find the cell where to insert the email. It store the various objects inside a list
# that will be navigated in order to find the correct one
emailElem = driver.find_elements_by_id('email')

# The second entry of the list is the correct one so send the email to it
emailElem[1].send_keys(Data.PacktEmailUnOff)

# Find the cell where to insert the password. It store the various objects inside a list
# that will be navigated in order to find the correct one
passwordElem = driver.find_elements_by_id('password')

# The second entry of the list is the correct one so send the password to it
passwordElem[1].send_keys(Data.PacktPasswordUnOff)

# Click the login button
passwordElem[1].submit()

'''
From now on it works theoretically but the recaptcha blocks the access

# Find the claim free book button, store again the results on a list
takeBook = driver.find_elements_by_id('free-learning-claim')

# Click it
takeBook[0].click()

# Stop the browser execution
driver.quit()
'''
