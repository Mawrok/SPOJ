# https://pl.spoj.com/problems/CALC/
from sys import stdin
from operator import *

for line in stdin:
    op, num1, num2 = line.split()
    print({'+': add, '-': sub, '*': mul, '/': floordiv, '%': mod}[op](int(num1), int(num2)))
