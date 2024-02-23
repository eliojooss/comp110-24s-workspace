"""Summing the elements of a list using diferent loops!"""


__author__ = "730484781"


def w_sum(vals1: list[float]) -> float:
    """Sum with while!"""
    counter1 = 0
    sum1: float = 0.0
    while counter1 < len(vals1):
        sum1 += vals1[counter1]
        counter1 += 1
    return sum1


def f_sum(vals2: list[float]) -> float:
    """Sum with for!"""
    sum2: float = 0.0
    for value in vals2:
        sum2 += value
    return sum2


def f_range_sum(vals3: list[float]) -> float:
    """Sum with for in range!"""
    sum3: float = 0.0
    for idx in range(0, len(vals3)):
        sum3 += vals3[idx]
    return sum3