t = int(input())
for _ in range(t):
    k, a, b, x, y = map(int, input().split())
    if x > y:
        x, y = y, x
        a, b = b, a
        
    cnt = 0
    if k >= a:
        div = 1 + (k - a) // x
        cnt += div
        k -= div * x

    if k >= b:
        cnt += 1 + (k - b) // y

    print(cnt)
