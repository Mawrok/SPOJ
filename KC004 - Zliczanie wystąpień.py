# https://pl.spoj.com/problems/KC004/
from sys import stdin

for line in stdin:
    find, count, *numbers = map(int, line.rstrip().split(" "))
    print(numbers.count(find))
