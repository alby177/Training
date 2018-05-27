from selenium import webdriver

# Webdriver executable file path
chrome_path ='D:\Alby\Programming\Training\chromedriver.exe'

# Add the path where the file with login credentials are
sys.path.append('/Volumes/StorEDGE/Alby/Python/Sensible_documents')

# Import the file with the credentials
import Data

# Open a Chrome browser
driver = webdriver.Chrome(chrome_path)

#  Navigate to webpage
driver.get('https://forum.codesys.com/')

login = driver.find_element_by_link_text("Login")
login.click()

emailElem = driver.find_element_by_name("username")

emailElem.send_keys(Data.CodesysUser)

passwordElem = driver.find_element_by_name('password')

passwordElem.send_keys(Data.CodesysPassword)

goIn = driver.find_element_by_name("login")
goIn.click()

notification = driver.find_element_by_id("notification_list_button")

print(notification.text)

# Close the browser
driver.quit()
