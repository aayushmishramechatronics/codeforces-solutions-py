import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))

chocolates = [0] * (n + 2)
for i in range(1, n + 1):
    chocolates[i] = chocolates[i - 1] + times[i - 1]
chocolates[n + 1] = chocolates[n]

left, right = 0, n + 1

while right > left:
    alice = chocolates[left]
    bob = chocolates[n + 1] - chocolates[right]

    if alice <= bob:
        left += 1
    else:
        right -= 1

print(left, n - left)
