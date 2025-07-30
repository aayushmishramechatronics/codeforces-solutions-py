import math
import sys
def solve():
    try:
        line = sys.stdin.readline()
        if not line:
            return
        n, c = map(int, line.split())
        a = list(map(int, sys.stdin.readline().split()))

        deadlines = []
        for val in a:
            if val > c:
                deadlines.append(0)
            else:
                deadline = math.floor(1 + math.log2(c / val))
                deadlines.append(deadline)
        
        deadlines.sort()
        
        free_bags_count = 0
        for d in deadlines:
            if free_bags_count + 1 <= d:
                free_bags_count += 1
        
        print(n - free_bags_count)

    except (IOError, ValueError):
        return

def main():
    try:
        line = sys.stdin.readline()
        if line.strip():
            t = int(line)
            for _ in range(t):
                solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()
