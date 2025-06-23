t = int(input())
for _ in range(t):
    n = int(input())
    v = [0] * (2 * n + 1)
    w = [True] * (2 * n + 1)

    for row in range(1, n + 1):
        row_data = list(map(int, input().split()))
        for col in range(1, n + 1):
            x = row_data[col - 1]
            w[x] = False
            v[row + col] = x

    for p in range(1, 2 * n + 1):
        if w[p]:
            v[1] = p
            break

    print(' '.join(map(str, v[1:2 * n + 1])))
