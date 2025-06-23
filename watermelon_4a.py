def is_divisible_weight(k):
    return k > 2 and k % 2 == 0

k = int(input())
print("YES" if is_divisible_weight(k) else "NO")
