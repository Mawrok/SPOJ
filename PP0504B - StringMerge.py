# https://pl.spoj.com/problems/PP0504B/
tests = int(input())
for i in range(tests):
    [first, second] = input().split()
    for j in range(min(len(first), len(second))):
        print(first[j], second[j], sep="", end="")
    print()
