# https://pl.spoj.com/problems/FR_07_01/
from sys import stdin
  
tests = int(input())
for i in range(tests):
    a, b = stdin.readline().split()
    print(max(int(a[::-1]), int(b[::-1]))) 
