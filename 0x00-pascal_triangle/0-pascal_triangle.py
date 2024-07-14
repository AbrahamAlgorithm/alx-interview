#!/usr/bin/python3
"""Solving Pascal Triangle"""


def pascal_triangle(n):
    """Solving of Pascal triangle"""
    if type(n) is not int:
        return ("n should be an integer")
    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    sub = []
    step = []
    final = []

    for i in range(1, n+1):
        if i == 1:
            final.append([1])
        elif i == 2:
            final.append([1, 1])
        elif i == 3:
            final.append([1, 2, 1])
        else:
            sub = final[i - 2]
            for j in range(1, len(sub) + 1):
                if j == 1:
                    step.append(1)
                if j == len(sub):
                    step.append(1)
                else:
                    step.append(sub[j-1] + sub[j])

        if i > 3:
            final.append(step)
            step = []
    return (final)
