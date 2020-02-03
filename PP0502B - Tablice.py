# https://pl.spoj.com/problems/PP0502B/
tests = int(input())
for i in range(tests):
    print(*list(map(int, input().split()))[:0:-1])
