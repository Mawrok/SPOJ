# https://pl.spoj.com/problems/FR_09_06/
tests = int(input())
for i in range(tests):
    word = input()
    ord_compare = lambda char: ord(char)
    print(ord(max(word, key = ord_compare)) - ord(min(word, key = ord_compare)))
