import kivy
kivy.require('1.9.0')

# Import the kivy application
from kivy.app import App

# Import the widget class which will be customized
from kivy.uix.pagelayout import PageLayout

# Creating the class that will be instanced as object
class PageLayoutApp(App):

    # Constructor of the class that will launch the window
    def build(self):
        return PageLayout()

# Create the object
plApp = PageLayoutApp()

# Run the application
plApp.run()
