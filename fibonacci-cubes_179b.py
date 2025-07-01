def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        f, g = 1, 1
        for _ in range(2, n + 2):
            f, g = g, f + g

        result = []
        for _ in range(m):
            a, b, c = map(int, input().split())
            if a >= f and b >= f and c >= f and max(a, b, c) >= g:
                result.append('1')
            else:
                result.append('0')

        print(''.join(result))
        
solve()
