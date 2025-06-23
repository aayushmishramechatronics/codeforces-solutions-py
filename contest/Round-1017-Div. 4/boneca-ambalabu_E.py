def main():
    import sys
    input = sys.stdin.readline

    B = 35  
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        v = [0] * B  

        for num in a:
            x = num
            for b in range(B):
                if x == 0:
                    break
                v[b] += x % 2
                x //= 2

        max_beauty = 0
        for num in a:
            x = num
            total = 0
            for b in range(B):
                if x % 2 == 1:
                    total += (1 << b) * (n - v[b])  
                else:
                    total += (1 << b) * v[b]        
                x //= 2
            max_beauty = max(max_beauty, total)

        print(max_beauty)

if __name__ == "__main__":
    main()
