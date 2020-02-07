# https://pl.spoj.com/problems/ML2_A/
from math import sqrt

def is_prime(num):
    return num >= 2 and all(num % i for i in range(2, 1 + int(sqrt(num))))

tests = int(input())
for i in range(tests):
    num = int(input())
    for j in range(num):
        rest = num - j;
        if (is_prime(j) and is_prime(rest)):
            print("TAK", j, rest)
            break
    else:
        print("NIE")
