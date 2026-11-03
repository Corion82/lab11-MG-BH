# https://github.com/Corion82/lab11-MG-BH
# Partner 1: Matthew Gardstein
# Partner 2: Brent Hiser
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""

import math

# SQUARE ROOT
def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)

# HYPOTENUSE
def hypotenuse(a, b):
    return math.hypot(a, b)

# ADDING
def add(a, b):
    return a + b

# SUBTRACTING
def subtract(a, b):
    return a - b

# MULTIPLYING
def mul(a, b):
    return a * b

# DIVIDING
def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

# LOGARITHM
def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid argument for logarithm.")
    return math.log(b, a)

# EXPONENT
def exp(a, b):
    return a ** b
