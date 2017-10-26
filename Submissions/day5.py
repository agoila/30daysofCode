#!/bin/python3

import sys


n = int(input().strip())

for i in range(1, 11):
    prod = n * i
    print('{} x {} = {}'.format(n, i, prod))
