import kivy
kivy.require('1.9.0')

# Import the kivy application
from kivy.app import App

# Import the widget class which will be customized
from kivy.uix.floatlayout import FloatLayout

# Creating the class that will be instanced as object
class FloatingApp(App):

    # Constructor of the class that will launch the window
    def build(self):
        return FloatLayout()

# Create the object
flApp = FloatingApp()

# Run the application
flApp.run()
