# https://pl.spoj.com/problems/PP0502B/
tests = int(input())
for i in range(tests):
    numbers = list(map(int, input().split()))
    print(*numbers[:0:-1])
