#!/usr/bin/python3

"""
Function returning a list of lists of integers representing the 
Pascal triangle of n
"""
def pascal_triangle(n):
    if (n <= 0):
        return []