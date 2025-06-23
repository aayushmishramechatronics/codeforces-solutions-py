a, m = map(int, input().split())
height = list(map(int, input().split()))

height.sort()

i1, i2 = 0, 1
ways = 0

while i2 < a:
    if height[i2] - height[i1] <= m:
        ways += (i2 - i1)
        i2 += 1
    else:
        i1 += 1

ways *= 2
print(ways)
