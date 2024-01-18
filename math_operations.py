# math_operations

class MathOperations:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot perform modulo with zero divisor")
        return a % b

    def power(self, base, exponent):
        return base ** exponent
