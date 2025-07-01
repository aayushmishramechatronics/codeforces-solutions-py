t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print((n + k - 3) // (k - 1))
