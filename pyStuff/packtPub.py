# Save the free book inside my account of PacktPub
from robobrowser import RoboBrowser
import re
import sys

# Add the path where the file with login credentials are
sys.path.append('/Volumes/StorEDGE/Alby/Python/Sensible_documents')

# Import the file with the credentials
import Data

home = 'https://www.packtpub.com/'

# Get login page url
url = 'https://www.packtpub.com/packt/offers/free-learning#'

# Configure the web page opener and the web page parser
br = RoboBrowser(parser='html.parser', user_agent ='Mozilla/5.0')

# Open the web page
br.open(url)

# Get the part of the page where to put the login information identified as "form"
form = br.get_form('packt-user-login-form')

# Insert username and password in the
form['email'] = Data.PacktEmailUnOff
form['password'] = Data.PacktPasswordUnOff

# Click the button to log as user
br.submit_form(form)

''' The following part of the code theoretically work but the recaptcha of the
website blocks everything

# Look for the book claiming button
form2 = br.get_form('free-learning-form')

# Click on the form to take the book
br.submit_form(form2)
'''
