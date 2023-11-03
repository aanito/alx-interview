#!/usr/bin/python3
"""Solve nqueen problem by using recursion to backtrack
Rules attack diagonally, horizontally and vertical. Therefore
no two queens should be in the attack zone"""
from sys import argv


def check():
    """Checks if requirements are fulfiled"""
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    elif str.isdigit(argv[1]) is False:
        print("N must be a number")
        exit(1)
    elif int(argv[1]) < 4:
        print("N must be at least 4")
        exit(1)


check()
n = int(argv[1])


def nqueen(n):
    """Create board and call backtrack function"""
    col = set()
    p_diagonal = set()
    n_diagonal = set()
    result = []
    board = [["."] * n for i in range(n)]

    def backtrack(r):
        """Solve the possible place for the n queens without clashing
        through backtracking"""
        if r == n:
            copy = ["".join(row) for row in board]
            result.append(copy)
            return
        for c in range(n):
            if c in col or (r + c) in p_diagonal or (r - c) in n_diagonal:
                continue
            col.add(c)
            p_diagonal.add(r + c)
            n_diagonal.add(r - c)
            board[r][c] = "Q"
            backtrack(r + 1)
            col.remove(c)
            p_diagonal.remove(r + c)
            n_diagonal.remove(r - c)
            board[r][c] = "."
    backtrack(0)
    return result


nqueen = nqueen(n)
val = "Q"


"""Get the row and column where queen are placed without clashing"""
for sol in nqueen:
    my_result = [[index, row.index(val)]
                 for index, row in enumerate(sol) if val in row]
    print(my_result)
    