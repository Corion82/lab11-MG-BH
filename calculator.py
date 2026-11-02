# https://github.com/Corion82/lab11-MG-BH
# Partner 1: Matthew Gardstein
# Partner 2: Brent Hiser
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# ADDING
def add(a, b):
    return a + b

# SUBTRACTING
def subtract(a, b):
    return a - b

# MULTIPLYING
def multiply(a, b):
    return a * b

# DIVIDING
def divide(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

# LOGARITHM
def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid argument for logarithm.")
    return math.log(b, a)

# EXPONENT
def exponent(a, b):
    return a ** b