'''
Calculator project made with kivy
'''

import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

# Define the calculator layout
class CalcGridLayout(GridLayout):

    # Create the function responsible for the calculation
    def Calculate(self, calculation):

        # Check if something is displayed on the calculator screen
        if calculation:
            try:
                # eval(param) transform the passed string param and evaluate it as code
                # execute the calculation if possible and put the result into a string
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

# Create the application calculator
class CalculatorApp(App):

    # When the object is created, insert the CalcGridLayout
    def build(self):
        return CalcGridLayout()

# Create the calculator object
calcApp = CalculatorApp()

# Run the calculator app
calcApp.run()
