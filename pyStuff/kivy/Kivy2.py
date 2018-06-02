# This time we separate the logic layer from the presentation layer, here there is the logic layer
# while in the "HelloKivi.kv" there is the presentation layer
import kivy
kivy.require('1.9.0')

# Import the kivy application
from kivy.app import App

# Import the Label object
from kivy.uix.button import Label

# Define a class that inherits from App
class HelloKivyApp(App):

    # Define the constructor that will create a window and display the presentation layer
    # created in the "HelloKivy.kv"
    def build(self):
        return Label()

# Create the object
helloKivy = HelloKivyApp();

# Run the object
helloKivy.run()
