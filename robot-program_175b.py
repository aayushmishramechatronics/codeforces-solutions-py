t = int(input())
for _ in range(t):
    n, x, k = map(int, input().split())
    s = input()
    
    for p in range(min(k, len(s))):
        if s[p] == 'R':
            x += 1
        elif s[p] == 'L':
            x -= 1
        k -= 1
        if x == 0:
            break

    if x != 0:
        print(0)
        continue

    resultant = 1
    position = 0
    for i in range(n):
        if s[i] == 'R':
            position += 1
        elif s[i] == 'L':
            position -= 1

        if position == 0:
            resultant += k // (i + 1)
            break

    print(resultant)
