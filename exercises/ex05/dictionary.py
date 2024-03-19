"""EX05 Dictionaries and Functions!"""

__author__ = "730484781"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert a dictionary!"""
    inverted = {}
    for key in dictionary:
        if dictionary[key] in inverted:
            raise KeyError("Error repeated values!")
        inverted[dictionary[key]] = key 
    return inverted


def favorite_color(dictionary: dict[str, str]) -> str:
    """Find the favorite color in a list of responses!"""
    color_num: dict[str, int] = {}
    highest_number = 0

    for key in dictionary:
        if dictionary[key] in color_num:
            color_num[dictionary[key]] += 1
        else:
            color_num[dictionary[key]] = 1

    for key in color_num:
        if color_num[key] > highest_number:
            highest_number = color_num[key]

    for key in color_num:
        if color_num[key] == highest_number:
            return key
    
    return "Error"


def count(my_list: list[str]) -> dict[str, int]:
    """Count number of appearances in a string!"""
    return_dict: dict[str, int] = {}
    for i in my_list:
        if i in return_dict:
            return_dict[i] += 1
        else:
            return_dict[i] = 1   
    return return_dict


def alphabetizer(my_list: list[str]) -> dict[str, list[str]]:
    """Alphabetize a list!"""
    return_dict: dict[str, list[str]] = {}
    for i in my_list:
        first_letter: str = i[0].lower()
        if first_letter in return_dict:
            return_dict[first_letter].append(i)
        else:
            return_dict[first_letter] = [i]
    return return_dict


def update_attendance(attendance: dict[str, list[str]], day: str, person: str) -> None:
    """Update attendance!"""
    if day in attendance:
        if person not in attendance[day]:
            attendance[day].append(person)
    else:
        attendance[day] = [person]