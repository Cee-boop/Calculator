from valid_inputs import if_valid
import sys
from math import sqrt
from random import choice


# calculator functions:
def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


def power_of(num1, num2):
    return num1 ** num2


def root(number):
    return sqrt(number)


# main program ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def cont(total_sum):
    """If user is running a continuous calculation. """

    operator = input("Pick an operation: ")

    if operator == "^":
        square_root = root(total_sum)
        new_number()

    # check operator symbol is valid:
    valid = if_valid(operator)
    if not valid:
        print("Operator symbol not valid.")
        cont(total_sum)

    next_number = float(input("What's the next number: "))
    operations(total_sum, next_number, operator)


def operations(first_number, second_number, operator_symbol):
    """A portal to pass through both numbers to correct operator
        using a dictionary to store the final sum."""

    operators = {
        "/": divide(first_number, second_number),
        "*": multiply(first_number, second_number),
        "-": subtract(first_number, second_number),
        "+": add(first_number, second_number),
        "**": power_of(first_number, second_number)
     }

    total = operators[operator_symbol]
    result(first_number, second_number, total, operator_symbol)


def result(num1, num2, total_sum, operator):
    """Prints the total sum and asks user if they want to continue
        using the current sum in another calculation."""

    print(f'{num1} {operator} {num2} = {total_sum}')
    still_continue = input(f'Type "y" to continue calculating with {total_sum}, "e" to exit, '
                                    f'or "new" to start a new calculation: ').lower()

    if still_continue == "e":
        statements = ["Goodbye!", "Cya!", "Laters!", "Sayonara!", "Dueces!", "Toodles!"]
        print(choice(statements))
        sys.exit()
    if still_continue == "y":
        cont(total_sum)
    if still_continue == "new":
        new_number()


def new_number():
    """Starts a new calculation."""

    first_number = float(input("What's the first number: "))
    operator = (input("+\n-\n/\n*\n**\n^\nPick an operation: "))

    if operator == "^":
        square_root = root(first_number)
        print(f"The square root of {first_number} is: {square_root}")
        new_number()

    # check operator symbol is valid:
    checker = ["+", "-", "/", "*", "**"]
    while operator not in checker:
        operator = input("+   -  **  /  *\nPick an operation: ")
        valid = if_valid(operator)

        if not valid:
            print("Operator not valid.")

    second_number = float(input("What's the second number: "))
    operations(first_number, second_number, operator)


new_number()





