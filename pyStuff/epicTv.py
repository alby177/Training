from robobrowser import RoboBrowser
import re
import sys

# Add the path where the file with login credentials are
sys.path.append('/Volumes/StorEDGE/Alby/Python/Sensible_documents')

# Import the file with the credentials
import Data

# Get login page url
url = 'https://shop.epictv.it/it?'

# Configure the web page opener and the web page parser
br = RoboBrowser(parser='html.parser', user_agent ='Mozilla/5.0')

# Open the web page
br.open(url)

# Get the part of the page where to put the login information identified as "form"
form = br.select('a')

br.submit_form(form[9])

form2 = br.get_form('epictv-commerce-user-combined-login-form')

# Insert username and password in the form
form2['edit-signin-email'] = Data.epicTvEmail
form2['edit-signin-password'] = Data.epicTvPassword

button = get_form('edit-signin-button')

br.submit_form(button)
