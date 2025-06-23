a = int(input())
for _ in range(a):
    k, x = map(int, input().split())
    idx = -1
    possible = True
    s_list = list(map(int, input().split()))
    
    for p in range(k):
        s = s_list[p]
        if idx < 0 and s:
            idx = p
        if s and idx + x <= p:
            possible = False

    print("YES" if possible else "NO")
