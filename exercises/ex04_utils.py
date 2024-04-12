"""EX04 - Utils!"""


__author__ = "730484781"


def all(list: list[int], int: int) -> bool:
    """Check if all values in a list are equal to a chose integer!"""
    counter = 0

    if len(list) == 0:
        return False
    else:
        while counter < len(list):
            if list[counter] == int:
                counter += 1
            else:
                return False
        return True


def max(input: list[int]) -> int:
    """Find max value in a list!"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    
    counter: int = 0
    current_max: int = input[0]

    while counter < len(input):
        if input[counter] > current_max:
            current_max = input[counter]
        counter += 1
    return current_max


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Find out if two lists are perfectly equal to each other!"""
    return_value = True
    if len(list1) != len(list2):
        return False
    else:
        for i in range(0, len(list1)):
            if list1[i] != list2[i]:
                return_value = False
        return return_value
            

def extend(list1: list[int], list2: list[int]) -> None:
    """Appends the values from a second list to an initial list!"""   
    for i in list2:
        list1.append(i)
