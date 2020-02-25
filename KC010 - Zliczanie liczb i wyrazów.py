# https://pl.spoj.com/problems/KC010/
from sys import stdin

for line in stdin:
    words = line.split()
    numberCount = sum(map(str.isdigit, words))
    print(numberCount, len(words) - numberCount)
