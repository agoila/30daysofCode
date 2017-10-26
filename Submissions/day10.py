#!/bin/python3

import sys


n = int(input().strip())
d_to_b = []
rem = 0
ct = 0
inv = 0
while n > 0:
    rem = n % 2
    n = n // 2
    if rem == 1:
        ct += 1
        if ct >= inv:
            inv = ct
    else:
        ct = 0

print(inv)
    

    
