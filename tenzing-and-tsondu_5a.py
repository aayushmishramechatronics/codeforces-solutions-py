t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x = sum(a)
    y = sum(b)
    if x == y:
        print("Draw")
    elif x > y:
        print("Tsondu")
    else:
        print("Tenzing")
