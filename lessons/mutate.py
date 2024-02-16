"""Mutating functions."""

__author__ = "730484781"


def manual_append(list: list[int], num: int) -> None:
    """Append a list and an int."""
    list.append(num)


def double(list: list[int]) -> None:
    """Double a list."""
    counter: int = 0
    while counter < len(list):
        list[counter] *= 2
        counter += 1
