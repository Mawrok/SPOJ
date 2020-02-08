# https://pl.spoj.com/problems/PP0506A/
for i in range(int(input())):
    points = []
    for j in range(int(input())):
        name, x, y = input().split()
        points.append((name, int(x), int(y)))
    points.sort(key=lambda lst: lst[1] ** 2 + lst[2] ** 2)
    for lst in points:
        print(*lst)
    input()
