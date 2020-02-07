# https://pl.spoj.com/problems/VSR/
tests = int(input())
for i in range(tests):
    v1, v2 = map(int, input().split())
    print(2 * v1 * v2 // (v1+v2))  
