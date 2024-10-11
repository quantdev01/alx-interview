#!/usr/bin/python3
"""
documentation
"""


def island_perimeter(grid):
    """
    docu
    """
    perimeter = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                # Check the surrounding sides of the land cell
                if row == 0 or grid[row-1][col] == 0:  # Top
                    perimeter += 1
                if row == len(grid) - 1 or grid[row+1][col] == 0:  # Bottom
                    perimeter += 1
                if col == 0 or grid[row][col-1] == 0:  # Left
                    perimeter += 1
                if col == len(grid[0]) - 1 or grid[row][col+1] == 0:  # Right
                    perimeter += 1
    return perimeter
