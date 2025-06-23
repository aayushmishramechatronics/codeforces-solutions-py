t = int(input())
for _ in range(t):
    n = int(input())
    v = list(map(int, input().split()))
    v.sort()

    cnt1 = 0
    for p in range(n):
        if (v[p] + v[-1]) % 2 == 1:
            cnt1 += 1
        else:
            break

    cnt2 = 0
    for p in range(n - 1, -1, -1):
        if (v[0] + v[p]) % 2 == 1:
            cnt2 += 1
        else:
            break

    print(min(cnt1, cnt2))
