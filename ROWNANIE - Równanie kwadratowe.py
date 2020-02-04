# https://pl.spoj.com/problems/ROWNANIE/
from sys import stdin

for line in stdin:
    [a, b, c] = map(float, line.split())
    discriminant = b * b - 4 * a * c
    print(1 + int(discriminant > 0) - int(discriminant < 0))
