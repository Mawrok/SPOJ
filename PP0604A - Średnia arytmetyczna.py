# https://pl.spoj.com/problems/PP0604A/
from statistics import mean

tests = int(input())
for i in range(tests):
    count, *numbers = map(int, input().split())
    avg = mean(numbers)
    print(min(numbers, key = lambda arg: abs(avg - arg)))
