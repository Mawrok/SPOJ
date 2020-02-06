# https://pl.spoj.com/problems/PRZEDSZK/
from fractions import gcd
 
tests = int(input())
for i in range(tests):
    a, b = map(int, input().split())
    print(a * b // gcd(a, b))
