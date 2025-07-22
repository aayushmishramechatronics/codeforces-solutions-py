import sys
import math
def solve():
    a, b, k = map(int, sys.stdin.readline().split())
    common_divisor = math.gcd(a, b)
    required_dx = a // common_divisor
    required_dy = b // common_divisor
    
    if max(required_dx, required_dy) <= k:
        print(1)
    else:
        print(2)

def main():
    try:
        num_test_cases = int(sys.stdin.readline())
        for _ in range(num_test_cases):
            solve()
    except (ValueError, IndexError):
        return

if __name__ == "__main__":
    main()
