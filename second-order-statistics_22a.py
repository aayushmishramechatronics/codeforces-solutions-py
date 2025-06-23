k = int(input())
a = list(map(int, input().split()))

x = min(a)
value2 = x

for num in a:
    if num > x:
        if value2 == x or num < value2:
            value2 = num

if value2 != x:
    print(value2)
else:
    print("NO")
