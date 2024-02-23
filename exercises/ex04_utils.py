"""EX04 - Utils!"""

__author__ = "730484781"

def all(list: list[int], int: int) -> bool:
    counter: int = 0
    while counter < len(list):
        if list[counter] == int:
            counter += 1
        else:
            return False
    return True

def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    counter: int = 0
    current_max: int = input[0]

    while counter < len(input):
        if input[counter] > current_max:
            current_max = input[counter]
        counter += 1
    return current_max
            



