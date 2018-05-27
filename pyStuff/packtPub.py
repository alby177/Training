from robobrowser import RoboBrowser
import re

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
form['email'] = Data.CodesysUser
form['password'] = Data.CodesysPassword

# Click the button to log as user
br.submit_form(form)

form2 = br.get_form('free-learning-form')
print(form2)
br.submit_form(form2)

#src = u''.join(str(br.parsed())).encode('utf-8')

#print(src)
