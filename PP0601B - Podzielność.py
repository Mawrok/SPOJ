# https://pl.spoj.com/problems/PP0601B/
tests = int(input())
for i in range(tests):
    n, x, y = map(int, input().split())
    for j in range(n):
        if j % x == 0 and j % y != 0:
            print(j, end=" ")
    print()
