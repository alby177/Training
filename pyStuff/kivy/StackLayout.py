import kivy
kivy.require('1.9.0')

# Import the kivy application
from kivy.app import App

# Import the widget class which will be customized
from kivy.uix.stacklayout import StackLayout

# Creating the class that will be instanced as object
class StackLayoutApp(App):

    # Constructor of the class that will launch the window
    def build(self):
        return StackLayout()

# Create the object
stApp = StackLayoutApp()

# Run the application
stApp.run()
