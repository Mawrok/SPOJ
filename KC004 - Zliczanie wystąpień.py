# https://pl.spoj.com/problems/KC004/
while True:
    try:
        numbers = list(map(int, input().split()))
        print(numbers[2:].count(numbers[0]))
    except EOFError:
        break
