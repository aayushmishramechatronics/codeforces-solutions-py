a, k = map(int, input().split())

meet = True
prev = '*'

for _ in range(a):
    color = input()
    
    if color[0] == prev:
        meet = False
        break

    prev = color[0]

    for i in range(1, k):
        if color[i] != color[0]:
            meet = False
            break

    if not meet:
        break

print("YES" if meet else "NO")
