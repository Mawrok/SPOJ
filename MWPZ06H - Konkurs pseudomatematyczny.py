# https://pl.spoj.com/problems/MWPZ06H/
from bisect import bisect_left

tests = int(input())
for i in range(tests):
    _, numbers = input(), sorted(map(int, input().split()))
    idx = bisect_left(numbers, numbers[-1])
    print(*(numbers[idx:] + numbers[:idx]))
