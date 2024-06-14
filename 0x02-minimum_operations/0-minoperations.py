#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
    Calc the fewest numb of operations needed
    """
    if n <= 1:
        return (0)

    operations = 0
    current_chars = 1
    clipboard = 0

    while current_chars < n:
        if current_chars >= n // 2:
            clipboard = current_chars
        else:
            if clipboard == current_chars:
                clipboard = 0
            current_chars += clipboard
            operations += 2
            clipboard = current_chars

    return (operations + 1)
