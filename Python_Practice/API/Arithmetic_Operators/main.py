"""
   main.py
   
   this module is basic structure of web api

   Here we calculate some arithmetic operators api with methods

   addition
   subraction
   multiplication
   divison
   mod

    Returns:
        init : arithmatic
"""

# from typing import Union

from fastapi import FastAPI

# create a fast API instance
app = FastAPI()

@app.get("/calculate/add/{number1}/{number2}")
def add(number1: int, number2: int):
    """This is addition implementation

    Args:
        number1 (int): pass the first number
        number2 (int): pass the second number

    Returns:
        int: number1 and number2
    """
    return number1 + number2

@app.get("/calculate/sub/{number1}/{number2}")
def add(number1: int, number2: int):
    """This is subraction implementation

    Args:
        number1 (int): pass the first number
        number2 (int): pass the second number

    Returns:
        int: number1 and number2
    """
    return number1 - number2

@app.get("/calculate/mul/{number1}/{number2}")
def add(number1: int, number2: int):
    """This is multiplication implementation

    Args:
        number1 (int): pass the first number
        number2 (int): pass the second number

    Returns:
        int: number1 and number2
    """
    return number1 * number2

@app.get("/calculate/div/{number1}/{number2}")
def add(number1: int, number2: int):
    """This is division implementation

    Args:
        number1 (int): pass the first number
        number2 (int): pass the second number

    Returns:
        int: number1 and number2
    """
    return number1 // number2

@app.get("/calculate/mod/{number1}/{number2}")
def add(number1: int, number2: int):
    """This is mod implementation

    Args:
        number1 (int): pass the first number
        number2 (int): pass the second number

    Returns:
        int: number1 and number2
    """
    return number1 % number2
