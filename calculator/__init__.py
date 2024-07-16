# Import essential modules
from calculator.calculation import Calculation
from calculator.operations import add,subtract,multiply,divide

# Definition of Calculator class
class Calculator:
    @staticmethod
    def add(a,b):
        # Create a Calculation object and return result from add
        calc = Calculation(a,b,add)
        return calc.get_result()
    
    @staticmethod
    def subtract(a,b):
        # Create a Calculation object and return result from subtract
        calc = Calculation(a,b, subtract)
        return calc.get_result()
    
    @staticmethod
    def multiply(a,b):
        # Create a Calculation object and return result from multiply
        calc = Calculation(a,b,multiply)
        return calc.get_result()
    
    @staticmethod
    def divide(a,b):
        # Create a Calculation object and return result from divide
        calc = Calculation(a,b,divide)
        return calc.get_result()
    
