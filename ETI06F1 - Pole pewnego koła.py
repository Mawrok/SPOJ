# https://pl.spoj.com/problems/ETI06F1/
from math import pi
radius, distance = map(float, input().split())
print(pi * (radius ** 2 - distance ** 2 / 4))
