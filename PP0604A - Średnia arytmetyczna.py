# https://pl.spoj.com/problems/PP0604A/

from statistics import mean

tests = int(input())
for i in range(tests):
    numbers = list(map(int, input().split()))
    numbers.pop(0)
    avg = mean(numbers)
    print(min(numbers, key = lambda arg: abs(avg - arg)))
