import sys

def solve():
    try:
        n, j, k = map(int, sys.stdin.readline().split())
        a = list(map(int, sys.stdin.readline().split()))
        j -= 1
        strength_j = a[j]
        other_strengths = []
        for i in range(n):
            if i != j:
                other_strengths.append(a[i])
        other_strengths.sort(reverse=True)
        if k == 0:
            print("NO")
            return

        coalition_strengths = [strength_j]
        if k > 1:
            coalition_strengths.extend(other_strengths[:k-1])
            
        elimination_strengths = other_strengths[k-1:]
        if not elimination_strengths:
            print("YES")
            return
            
        max_coalition_strength = max(coalition_strengths)
        max_elimination_strength = max(elimination_strengths)
        if max_coalition_strength >= max_elimination_strength:
            print("YES")
        else:
            print("NO")

    except (IOError, ValueError):
        return

def main():
    try:

        num_test_cases = int(sys.stdin.readline())
        for _ in range(num_test_cases):
            solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()
