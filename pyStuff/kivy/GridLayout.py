import kivy
kivy.require('1.9.0')

# Import the kivy application
from kivy.app import App

# Import the widget class which will be customized
from kivy.uix.gridlayout import GridLayout

# Creating the class that will be instanced as object
class GridLayoutApp(App):

    # Constructor of the class that will launch the window
    def build(self):
        return GridLayout()

# Create the object
grApp = GridLayoutApp()

# Run the application
grApp.run()
