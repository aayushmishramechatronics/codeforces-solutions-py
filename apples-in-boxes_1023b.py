t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    mna = float('inf')
    mxa = 0
    cntmx = 0
    s = 0

    for x in a:
        s = (s + x) % 2
        if x > mxa:
            mxa = x
            cntmx = 1
        elif x == mxa:
            cntmx += 1
        mna = min(mna, x)

    if (mxa > mna + k + 1) or ((mxa == mna + k + 1) and cntmx > 1):
        print("Jerry")
    else:
        print("Tom" if s else "Jerry")
