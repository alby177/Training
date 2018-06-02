import kivy
kivy.require('1.9.0')

# Import the kivy application
from kivy.app import App

# Import the widget class which will be customized
from kivy.uix.widget import Widget

# Build the custom widget that will be edited in the customWidget.kv file
class CustomWidget(Widget):
    pass # it contains just pass because the class could be the same as the father Widget

# Create the custom widget app the when reu returns the CustomWidget visualiziong the window with the buttons
class CustomWidgetApp(App):

    # Edit the constructor in order to return the window
    def build(self):
        return CustomWidget()

# Create the object from the custom class
customWidget = CustomWidgetApp()

# Run the object
customWidget.run()
