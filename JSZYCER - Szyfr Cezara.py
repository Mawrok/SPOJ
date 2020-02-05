# https://pl.spoj.com/problems/JSZYCER/
from sys import stdin
for line in stdin:
    line = line.rstrip()
    shift = 3
    start = ord('A')
    count = ord('Z') - ord('A') + 1
    caesar_cipher3 = lambda char: char if char == ' ' else chr((ord(char) + shift - start) % count + start)
    print(''.join(map(caesar_cipher3, line)))
