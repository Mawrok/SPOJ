# https://pl.spoj.com/problems/PP0501A/
from fractions import gcd

tests = int(input())
for i in range(tests):
    a, b = map(int, input().split())
    print(gcd(a, b))
