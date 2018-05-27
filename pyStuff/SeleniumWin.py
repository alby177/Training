# Log into the codesys forum and print how manu notifications there are on the profile
from selenium import webdriver

# Import system functions
import sys

# Include the path where to take the personal information
sys.path.append('/Volumes/StorEDGE/Alby/Python/Sensible_documents')

# Import the personal data file
import Data

# Webdriver executable file path
chrome_path ='D:\Alby\Programming\Training\chromedriver.exe'

# Open a Chrome browser
driver = webdriver.Chrome(chrome_path)

#  Navigate to webpage
driver.get('https://forum.codesys.com/')

# Find the login button on the page
login = driver.find_element_by_link_text("Login")

# Click the login button
login.click()

# Find the cell where to put username
emailElem = driver.find_element_by_name("username")

# Write the username
emailElem.send_keys(Data.CodesysUser)

# Find the cell where to put password
passwordElem = driver.find_element_by_name('password')

# Write the password
passwordElem.send_keys(Data.CodesysPassword)

# Find the login button
goIn = driver.find_element_by_name("login")

# Click the login button once when the form is filled
goIn.click()

# Find the notification field
notification = driver.find_element_by_id("notification_list_button")

# Extract and print the notifications amount
print(notification.text)

# Close the browser
driver.quit()
