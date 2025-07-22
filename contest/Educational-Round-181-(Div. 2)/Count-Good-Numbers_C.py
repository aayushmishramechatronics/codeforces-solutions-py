import sys
def count_good_numbers_upto(n):
    if n < 1:
        return 0
    
    bad_numbers = 0
    bad_numbers += (n // 2) + (n // 3) + (n // 5) + (n // 7)
    bad_numbers -= (n // 6) + (n // 10) + (n // 14) + (n // 15) + (n // 21) + (n // 35)
    bad_numbers += (n // 30) + (n // 42) + (n // 70) + (n // 105)
    bad_numbers -= n // 210

    return n - bad_numbers

def solve():
    try:
        l, r = map(int, sys.stdin.readline().split())
        answer = count_good_numbers_upto(r) - count_good_numbers_upto(l - 1)
        print(answer)
    except (ValueError, IndexError):
        return

def main():
    try:
        num_test_cases = int(sys.stdin.readline())
    except (ValueError, IndexError):
        return

    for _ in range(num_test_cases):
        solve()

if __name__ == "__main__":
    main()
