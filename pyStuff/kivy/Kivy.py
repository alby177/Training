# Script to understand if everything works correctly and display a windows with a label inside
# REMEMBER TO RUN THE SCRIPT FROM THE TERMINAL AS: $ kivy <filename>
import kivy
kivy.require('1.9.0')

# Import the kivy application
from kivy.app import App

# Import the Label object
from kivy.uix.button import Label

# Define a class that inherits from App
class HelloKivy(App):

    # Define the function build that will create a window and display "Hello Kivy"
    def build(self):
        return Label(text = 'Hello Kivy')

# Create the object
helloKivy = HelloKivy();

# Run the object
helloKivy.run()
