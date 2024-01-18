# main.py

from math_operations import MathOperations


def main():
    calculator = MathOperations()

    while True:
        user_input = input("Enter 'O' for Yes, '*' for No for Calculation: ")
        if user_input.lower() != 'o':
            break

        expression = input("Enter the calculation: ")

        try:
            result = evaluate_expression(calculator, expression)
            print(f"Result: {result}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
        except Exception as e:
            print(f"Error: {e}")


def evaluate_expression(calculator, expression):
    current_result = 0
    current_operator = '+'
    num = 0

    for char in expression:
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in ('+', '-', '*', '/'):
            if current_operator == '+':
                current_result = calculator.add(current_result, num)
            elif current_operator == '-':
                current_result = calculator.subtract(current_result, num)
            elif current_operator == '*':
                current_result = calculator.multiply(current_result, num)
            elif current_operator == '/':
                current_result = calculator.divide(current_result, num)
            num = 0  # Reset num for the next number
            current_operator = char

    # Process the last number in the expression
    if current_operator == '+':
        current_result = calculator.add(current_result, num)
    elif current_operator == '-':
        current_result = calculator.subtract(current_result, num)
    elif current_operator == '*':
        current_result = calculator.multiply(current_result, num)
    elif current_operator == '/':
        current_result = calculator.divide(current_result, num)

    return current_result


if __name__ == "__main__":
    main()
