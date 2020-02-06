# https://pl.spoj.com/problems/PA05_POT/
tests = int(input())
for i in range(tests):
    base, exp = map(int, input().split())
    print((base % 10) ** ((exp - 1) % 4 + 1) % 10)
