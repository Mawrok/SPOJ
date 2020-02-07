# https://pl.spoj.com/problems/ETI06F1/
from math import pi
r, d = map(float, input().split())
print(pi * (r * r - d * d / 4))
