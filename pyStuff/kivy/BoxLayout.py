import kivy
kivy.require('1.9.0')

# Import the kivy application
from kivy.app import App

# Import the widget class which will be customized
from kivy.uix.boxlayout import BoxLayout

# Creating the class that will be instanced as object
class BoxLayoutApp(App):

    # Constructor of the class that will launch the window
    def build(self):
        return BoxLayout()

# Create the object
blApp = BoxLayoutApp()

# Run the application
blApp.run()
