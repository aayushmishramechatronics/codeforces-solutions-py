import sys
def solve():
    try:
        n, k = map(int, sys.stdin.readline().split())
        wheather_data = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + wheather_data[i]
    hike = 0
    currnt_day = 0
    while currnt_day <= n - k:
        end_of_window = currnt_day + k
        rain_in_window = prefix_sum[end_of_window] - prefix_sum[currnt_day]
        if rain_in_window == 0:
            hike += 1
            currnt_day += k + 1
        else:
            currnt_day += 1  
    print(hike)
def main():
    try:
        test_cases = int(sys.stdin.readline())
        for _ in range(test_cases):
            solve()
    except (IOError, ValueError):
        pass
if __name__ == "__main__":
    main()
