# https://pl.spoj.com/problems/KC008/
from sys import stdin

total_acc = 0
for line in stdin:
    acc = sum(map(int, line.split()))
    total_acc += acc
    print(acc)
print(total_acc)
