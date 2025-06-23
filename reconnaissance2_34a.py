k = int(input())
a = list(map(int, input().rstrip().split()))

min_difference = abs(a[0] - a[-1])
p1 = 1
p2 = k

for i in range(1, k):
    difference = abs(a[i] - a[i - 1])
    if difference < min_difference:
        min_difference = difference
        p1 = i + 1
        p2 = i

print(p1, p2)
