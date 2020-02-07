# https://pl.spoj.com/problems/AL_05_01/
from sys import stdin

for number in map(int, stdin):
    print(int(bin(number)[:1:-1], 2))
