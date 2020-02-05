# https://pl.spoj.com/problems/JGGHACK/
from sys import stdin
for line in stdin:
    line = line.rstrip()
    base = lambda char : ord(char) - ord('A')
    result = ''.join(chr(base(line[i]) + 16 * base(line[i + 1])) for i in range(0, len(line), 2))
    print(result)
