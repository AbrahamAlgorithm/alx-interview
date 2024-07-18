#!/usr/bin/python3
'''
Rotation of two-dimensional array
'''


def rotate_2d_matrix(matrix):
    '''
    Rotating a two dimentional array[matrix]
    '''
    n = len(matrix[0])
    duplicate = []
    for i in range(n):
        new_array = []
        for j in range(n):
            new_array.append(matrix[i][j])
        duplicate.append(new_array)
    for i in range(n):
        pos = n - 1
        for j in range(n):
            matrix[i][j] = duplicate[pos][i]
            pos -= 1
