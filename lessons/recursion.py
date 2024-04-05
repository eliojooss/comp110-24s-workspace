"""CQ Recursion!"""

__author__ = "730484781"


def f(n: int, k: int) -> int:
    """Recursive function!"""
    if n == 0:
        return 0
    else: 
        return (n - 1) * k + k