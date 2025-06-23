t = int(input())
for _ in range(t):
    a, b, c = map(int, input().split())
    s = a + b + c
    u = -1 if s % 3 else s // 3
    print("YES" if u >= a and u >= b else "NO")
