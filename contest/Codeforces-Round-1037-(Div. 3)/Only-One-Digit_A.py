def solve():
    x_str = input()
    print(min(x_str))

def main():
    try:
        num_test_case = int(input())
        for _ in range(num_test_case):
            solve()
    except (ValueError, IndexError):
        pass

if __name__ == "__main__":
    main()
