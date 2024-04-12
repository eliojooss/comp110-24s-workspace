<<<<<<< HEAD
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
=======
"""List utils."""

__author__ = 720310785

def all(inp: list[int], val: int) -> bool:
    """Tell if list is all one number."""
    idx: int = 0
    while idx < len(inp):
        if val != inp[idx]:
            return False
        idx += 1
    return True

def max(inp: list[int]) -> int:
    """Find max in list."""
    idx: int = 0
    if len(inp) == 0:
        raise ValueError("max() arg is an empty List")
    max_num: int = inp[0]
    while idx < len(inp):
        if inp[idx] > max_num:
            max_num = inp[idx]
        idx += 1
    return max_num

def is_equal(inp1: list[int], inp2: list[int]) -> bool:
    """Check if two lists are equal."""

    if len(inp1) != len(inp2):
        return False
    else:
        idx: int = 0
        while idx < len(inp1):
            if inp1[idx] != inp2[idx]:
                return False
            idx += 1
    return True

def extend(inp1: list[int], inp2: list[int]) -> None:
    idx: int = 0
    while idx < len(inp2):
        inp1.append(inp2[idx])
        idx += 1
>>>>>>> 2ef5de78e346e7cf4170e08810c73ab71f3465a1
