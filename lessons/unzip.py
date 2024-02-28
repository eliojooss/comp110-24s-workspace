"""Splitting a dictionary into two lists!"""

__author__ = "730484781"


def get_keys(dict: dict[str, int]) -> list[str]:
    """Make a list of the keys!"""
    return_list = []
    for key in dict:
        return_list.append(key)
    return return_list


def get_values(dict: dict[str, int]) -> list[int]:
    """Make a list of the values!"""
    return_list = []
    for key in dict:
        return_list.append(dict[key])
    return return_list