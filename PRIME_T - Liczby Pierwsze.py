# https://pl.spoj.com/problems/PRIME_T/
from math import sqrt

tests = int(input())
for i in range(tests):
    num = int(input())
    print(("NIE", "TAK")[num >= 2 and all(num % i for i in range(2, 1 + int(sqrt(num))))])
