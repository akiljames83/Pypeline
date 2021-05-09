"""
Helper functions for the sorting algorithms

"""

def less(a,b) -> bool:
    return a < b

def swap(array, i,j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp