"""Mutating functions."""

__author__ = "730484781"

def manual_append(list: list[int], num: int):
    list.append(num)

def double(list:list[int]):
    counter: int = 0
    while counter < len(list):
        list[counter] *= 2
        counter +=1
