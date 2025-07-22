import sys
import math
def gcd(a, b):
    return math.gcd(a, b)
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return (a * b) // gcd(a, b)
def solve():
    try:
        n_str = sys.stdin.readline()
        if not n_str: return
        n = int(n_str)
        p = list(map(int, sys.stdin.readline().split()))
        s = list(map(int, sys.stdin.readline().split()))
    except (IOError, ValueError):
        return

    if n == 1:
        if p[0] == s[0]:
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
        return
    
    if p[n-1] != s[0]:
        sys.stdout.write("NO\n")
        return

    if gcd(p[0], s[1]) != s[0]:
        sys.stdout.write("NO\n")
        return

    if gcd(p[n-2], s[n-1]) != p[n-1]:
        sys.stdout.write("NO\n")
        return

    for i in range(1, n - 1):
        candidate_a_i = lcm(p[i], s[i])
        
        if gcd(p[i-1], candidate_a_i) != p[i]:
            sys.stdout.write("NO\n")
            return
            
        if gcd(candidate_a_i, s[i+1]) != s[i]:
            sys.stdout.write("NO\n")
            return

    sys.stdout.write("YES\n")

def main():
    try:
        t_str = sys.stdin.readline()
        if not t_str: return
        t = int(t_str)
        for _ in range(t):
            solve()
    except (IOError, ValueError):
        return

if __name__ == "__main__":
    main()
