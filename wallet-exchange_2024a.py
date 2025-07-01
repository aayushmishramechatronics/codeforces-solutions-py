t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    a += b
    print("Alice" if a % 2 else "Bob")
