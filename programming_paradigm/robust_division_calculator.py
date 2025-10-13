#!/usr/bin/python3
"""
This module provides a function for robustly dividing two numbers,
handling common errors such as division by zero and non-numeric inputs.
"""

def safe_divide(numerator, denominator):
    """
    Safely divides a numerator by a denominator, handling potential errors.

    This function attempts to convert both inputs to floats and perform
    division. It catches and handles ValueError if inputs are not numeric
    and ZeroDivisionError if the denominator is zero.

    Args:
        numerator (str or int or float): The number to be divided.
        denominator (str or int or float): The number to divide by.

    Returns:
        str: A message containing the result of the division or an
             error message indicating the issue.
    """
    try:
        num = float(numerator)
        den = float(denominator)
        result = num / den
        return f"The result of the division is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."