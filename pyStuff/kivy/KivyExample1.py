import kivy
kivy.require('1.9.0')

# Import the kivy application
from kivy.app import App

# Import the widget class which will be customized
from kivy.uix.widget import Widget

class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):

    def build(self):
        return Custo mWidget()


customWidget = CustomWidgetApp()
customWidget.run()
