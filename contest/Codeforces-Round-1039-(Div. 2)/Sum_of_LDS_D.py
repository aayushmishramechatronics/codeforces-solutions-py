import sys
def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str:
            return
        n = int(n_str)
        p = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    if n == 0:
        print(0)
        return
    dp = [0] * (n + 1)
    dp[1] = 1
    total_sum = 1
    for i in range(2, n + 1):
        if p[i-2] > p[i-1]:
            dp[i] = dp[i-1] + i
        else:
            dp[i] = dp[i-2] + i
        total_sum += dp[i]
    print(total_sum)

def main():
    try:
        t_str = sys.stdin.readline()
        if t_str:
            t = int(t_str)
            for _ in range(t):
                solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()
