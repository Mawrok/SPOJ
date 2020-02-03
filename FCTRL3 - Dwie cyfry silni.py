# https://pl.spoj.com/problems/FCTRL3/
from math import factorial
 
tests = int(input())
for i in range(tests):
    num = int(input())
    print(" ".join(str(0 if num > 10 else factorial(num) % 100).zfill(2))) 
