import sys
def solve():
    s = sys.stdin.readline().strip()
    t_count = s.count('T')
    other_chars = sorted([char for char in s if char != 'T'])
    result = 'T' * t_count + "".join(other_chars)
    print(result)

def main():
    try:
        num_test_cases = int(sys.stdin.readline())
        for _ in range(num_test_cases):
            solve()
    except (ValueError, IndexError):
        return

if __name__ == "__main__":
    main()
