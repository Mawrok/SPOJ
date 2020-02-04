# https://pl.spoj.com/problems/JSPACE/
from sys import stdin

for line in stdin:
    words = line.split()
    print(words.pop(0), end="")
    for word in words:
        print(word.capitalize(), end="")
    print()
