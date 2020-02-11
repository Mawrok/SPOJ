## https://pl.spoj.com/problems/JSPACE/
from sys import stdin

for line in stdin:
    first, *words = line.rstrip().split()
    print(first, *[word.capitalize() for word in words], sep = '')
