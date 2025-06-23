def main():
    k = int(input())
    for _ in range(k):
        a, x, y = map(int, input().split())
        found = False
        for b in range(1, 101):  
            if b == a:
                continue
            if abs(b - x) < abs(a - x) and abs(b - y) < abs(a - y):
                found = True
                break
        print("YES" if found else "NO")

if __name__ == "__main__":
    main()
