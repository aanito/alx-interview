#!/usr/bin/python3
"""Given a number n, write a method that calculates
the fewest number of operations needed to
result in exactly n H characters in the file."""


def minOperations(n):
    """Calculate how many operations is needed to
    get to n"""
    num, num_of_operations, cp_paste_operation = 1, 0, 2
    paste_operation, flag, i, count = 1, 1, 0, 0
    increment = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049]
    if type(n) != int:
        raise TypeError('Expected Integer as parameter')
    if n <= 0:
        return 0
    while (num != n and num < n):
        count += 1
        if count == 100:
            return 0
        if flag == 1 and n - num > increment[i]:
            if num_of_operations == 0:
                num_of_operations = cp_paste_operation
                num = num + increment[i]
            else:
                num_of_operations = num_of_operations + cp_paste_operation
                if n - num > i:
                    i = i + 1
                while (increment[i] > n - num):
                    i = i - 1
                num = num + increment[i]
            flag = 0
        else:
            while (increment[i] > n - num):
                num_of_operations += 1
                i = i - 1
            num = num + increment[i]
            num_of_operations = num_of_operations + paste_operation
            flag = 1
    return num_of_operations

