t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    vl = list(map(int, input().split()))
    vr = list(map(int, input().split()))
    v = []
    total = 0
    
    for i in range(n):
        v.append(min(vl[i], vr[i]))
        total += vl[i] + vr[i]
        
    v.sort()
    for i in range(n - k):
        total -= v[i]
        
    total -= (v[n - k] - 1)
    print(total)
