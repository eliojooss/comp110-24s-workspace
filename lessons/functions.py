"""Demonstrates functions"""
from random import randint

x: str = print("Hello!")
print(x)

print(round(10.25))

z: int = randint(1,7)
print(z)

"""Example functions to learn definition and calling syntax"""

def my_max (number1: int, number2: int) -> int:
    """Returns the maximum value out of 2 numbers"""
    if number1 >= number2:
        return number1
    else:
        return number2

Max: int = my_max(3,7)
print(Max)

