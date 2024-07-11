from calculator.calculation import Calculation
from calculator.operations import add,subtract,multiply,divide

class Calculator:
    @staticmethod
    def add(a,b):
        calc = Calculation(a,b,add)
        return calc.get_result()
    
    @staticmethod
    def subtract(a,b):
        calc = Calculation(a,b, subtract)
        return calc.get_result()
    
    @staticmethod
    def multiply(a,b):
        calc = Calculation(a,b,multiply)
        return calc.get_result()
    
    @staticmethod
    def divide(a,b):
        calc = Calculation(a,b,divide)
        return calc.get_result()
    
    