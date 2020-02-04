# https://pl.spoj.com/problems/KC004/
from sys import stdin

for line in stdin:
    numbers = list(map(int, line.split()))
    print(numbers[2:].count(numbers[0]))
