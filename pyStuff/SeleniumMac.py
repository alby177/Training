
import os
import sys
import selenium
from selenium import webdriver
sys.path.append('/Volumes/StorEDGE/Alby/Python/Sensible_documents')
import Data

chromedriver = "/usr/local/bin/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.packtpub.com/packt/offers/free-learning")
try:
    logInPackt = driver.find_element_by_link_text("Log in")
except selenium.common.exceptions.NoSuchElementException:
    print("User already logged in")
    exit()

logInPackt.click()

emailElem = driver.find_elements_by_id('email')

emailElem[1].send_keys(Data.PacktEmailUnOff)

passwordElem = driver.find_elements_by_id('password')

passwordElem[1].send_keys(Data.PacktPasswordUnOff)

passwordElem[1].submit()

takeBook = driver.find_elements_by_id('free-learning-claim')

takeBook[0].submit()
#driver.quit()
