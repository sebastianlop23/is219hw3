# Definition of Calculation class
class Calculation:
    def __init__(self,a,b,operation):
        # Initialize constructor
        self.a = a
        self.b = b
        self.operation = operation
    def get_result(self):
        # Gather results from operation and return
        return self.operation(self.a, self.b)