#!/bin/python3

import sys


arr = []
for _ in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)
    
def hourglass(my_arr):
    """
    Takes in my_arr (6x6 array) and returns hourglass elements
    in a list of list
    """
    s_glass = []
    for i in range(len(my_arr) - 2):
        for j in range(len(my_arr) - 2):
            h_glass = []
            h_glass += my_arr[i][j:3+j]
            h_glass.append(my_arr[i+1][j+1])
            h_glass += my_arr[i+2][j:3+j]
            s_glass.append(h_glass)
    
    return s_glass

# sum hourglasses
h_glasses = hourglass(arr)
sum_vals = [sum(h_glasses[i]) for i in range(len(h_glasses))]

# return the max sum
print(max(sum_vals))