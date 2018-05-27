# This program use roboworwser to access the codesys web forum login page, log into it and
# take the number of notification that are found top-left inside the page
# For the function of robobrowser go to this link: http://robobrowser.readthedocs.io/en/latest/api.html#module-robobrowser.browser
from robobrowser import RoboBrowser
import re

# Get login page url
url = 'https://forum.codesys.com/ucp.php?mode=login&sid=fd0b74beb56684de55973af7096462d7'

# Configure the web page opener and the web page parser
br = RoboBrowser(parser='html.parser', user_agent ='Mozilla/5.0')

# Open the web page
br.open(url)

# Get the part of the page where to put the login information identified as "form"
form =br.get_form()

# Insert username and password in the
form['username'] = ''
form['password'] = ''

# Click the button to log as user
br.submit_form(form)

# Parse the page and save the html result as string
src = str(br.parsed())

# Save the beginning of the string where the data to visualize is
start = '<strong>'

# Save the end of the string where the data to visualize is
end = '</strong>'

# Save the data through regular expression search function. putting the data  to find and where to find it
result = re.search('%s(.*)%s' % (start, end), src).group(1)

# Print the amount of notification
print(result)
