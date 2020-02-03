# https://pl.spoj.com/problems/ROWNANIE/
while True:
    try:
        [a, b, c] = map(float, input().split())
        discriminant = b * b - 4 * a * c
        print(1 + int(discriminant > 0) - int(discriminant < 0))
    except EOFError:
        break
