# https://pl.spoj.com/problems/POL/
tests = int(input())
for i in range(tests):
    word = input()
    print(word[:len(word) // 2])
