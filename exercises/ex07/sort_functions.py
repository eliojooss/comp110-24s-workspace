"""Functions that implement sorting algorithms."""

__author__ = ""

def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm.
    Insert into an already sorted list."""
    for i in range(1, len(x)):
        last_val = x[i]
        z = i-1
        while z >= 0 and last_val < x[z]:    
            x[z+1] = x[z]
            z-= 1
            x[z+1] = last_val
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. 
    Repeatedly find the minimum and swap it."""
    for i in range(len(x)):
        min_index=i
        for z in range(i, len(x)):
           if x[z] < x[min_index]:
               min_index = z
        temp_var: int = x[i]
        x[i] = x[min_index]
        x[min_index] = temp_var
    return None
    