#!/usr/bin/python3
""" Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """ Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    """
    if not all(isinstance(row, list) for row in matrix) or not matrix:
        return
    rows, cols = len(matrix), len(matrix[0])
    matrix[:] = [[matrix[r][c] for r in range(rows - 1, -1, -1)]
                 for c in range(cols)]
