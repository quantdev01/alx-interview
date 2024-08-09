#!/usr/bin/python3

"""
Function returning a list of lists of integers representing the
Pascal triangle of n
"""


def pascal_triangle(n):
    """
    pascal triangle function
    """
    main_array = []
    if n <= 0:
        return []
    for i in range(n):
        if i == 0:
            main_array.append([1])
        elif i == 1:
            main_array.append([1, 1])
        if i > 1:
            temp_array = main_array[len(main_array) - 1]
            number_array = []
            for j in range(len(temp_array) - 1):
                if (j != len(main_array) - 1):
                    number = temp_array[j] + temp_array[j + 1]
                    number_array.append(number)
            main_array.append([1, *number_array, 1])

    return main_array
