# https://pl.spoj.com/problems/JZLICZ/
from collections import Counter

counts = Counter()
tests = int(input())
for i in range(tests):
    counts.update(Counter(input().replace(' ', '')))
for let, count in sorted(counts.items(), key=lambda keyval: (not keyval[0].islower(), keyval[0])):
    print(let, count)
