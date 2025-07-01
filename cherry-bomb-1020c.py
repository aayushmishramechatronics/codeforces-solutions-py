t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    left = 0
    right = 2 * k

    for i in range(n):
        curleft = a[i] + (0 if b[i] < 0 else b[i])
        left = max(left, curleft)
        curright = a[i] + (k if b[i] < 0 else b[i])
        right = min(right, curright)

    ans = max(0, right - left + 1)
    print(ans)
