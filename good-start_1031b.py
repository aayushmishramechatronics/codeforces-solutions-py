t = int(input())
for _ in range(t):
    w, h, a, b = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == x2:
        print("yEs" if abs(y1 - y2) % b == 0 else "NO")
    elif y1 == y2:
        print("yEs" if abs(x1 - x2) % a == 0 else "NO")
    else:
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        print("yEs" if (dx % a == 0 or dy % b == 0) else "NO")
