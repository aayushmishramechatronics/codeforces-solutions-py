import sys
def solve():
    try:
        line_nk = sys.stdin.readline().split()
        if not line_nk:
            return
        n, k = map(int, line_nk)
        k -= 1
        
        h = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    towers = sorted([(h[i], i) for i in range(n)])
    
    if n == 0:
        print("NO")
        return

    max_h_val = towers[-1][0]

    if h[k] == max_h_val:
        print("YES")
        return

    pos = {original_idx: sorted_idx for sorted_idx, (_, original_idx) in enumerate(towers)}
    start_pos = pos[k]
    
    l, r = start_pos, start_pos
    
    min_a = h[k]
    max_h_a = h[k]

    min_b = -h[k]
    max_h_b = h[k]

    for _ in range(n - 1):
        t_left = float('inf')
        if l > 0:
            next_h, _ = towers[l-1]
            time = -next_h + min_a
            if next_h >= time + 1 and max_h_a >= time:
                t_left = time
        
        t_right = float('inf')
        if r < n - 1:
            next_h, _ = towers[r+1]
            time = next_h + min_b
            if next_h >= time + 1 and max_h_b >= time:
                t_right = time

        if t_left == float('inf') and t_right == float('inf'):
            break

        if t_left <= t_right:
            l -= 1
            time_at_arrival = t_left
            curr_h, _ = towers[l]
        else:
            r += 1
            time_at_arrival = t_right
            curr_h, _ = towers[r]
            
        if curr_h == max_h_val:
            print("YES")
            return

        new_a = time_at_arrival + curr_h
        if new_a < min_a:
            min_a = new_a
            max_h_a = curr_h
        elif new_a == min_a:
            max_h_a = max(max_h_a, curr_h)

        new_b = time_at_arrival - curr_h
        if new_b < min_b:
            min_b = new_b
            max_h_b = curr_h
        elif new_b == min_b:
            max_h_b = max(max_h_b, curr_h)

    print("NO")


def main():
    line = sys.stdin.readline()
    if line.strip():
        try:
            num_test_cases = int(line)
            for _ in range(num_test_cases):
                solve()
        except (ValueError, IndexError):
            pass

if __name__ == "__main__":
    main()
