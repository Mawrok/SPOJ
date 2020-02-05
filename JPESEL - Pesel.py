# https://pl.spoj.com/problems/JPESEL/
from operator import mul
weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1]
tests = int(input())
for i in range(tests):
    pesel = map(int, input())
    is_valid = sum(map(mul, pesel, weights)) % 10 == 0
    print(("N", "D")[is_valid])
