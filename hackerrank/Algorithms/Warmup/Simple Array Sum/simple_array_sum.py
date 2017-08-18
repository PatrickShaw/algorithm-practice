#!/bin/python3

import sys


n = int(input().strip())
print(sum((int(arr_temp) for arr_temp in input().strip().split(' '))))
