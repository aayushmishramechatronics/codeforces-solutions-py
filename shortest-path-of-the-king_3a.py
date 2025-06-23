s = input()
t = input()

print(max(abs(ord(s[0]) - ord(t[0])), abs(ord(s[1]) - ord(t[1]))))

while s != t:
    move = ''
    if s[0] < t[0]:
        move += 'R'
        s = chr(ord(s[0]) + 1) + s[1]
    elif s[0] > t[0]:
        move += 'L'
        s = chr(ord(s[0]) - 1) + s[1]

    if s[1] < t[1]:
        move += 'U'
        s = s[0] + chr(ord(s[1]) + 1)
    elif s[1] > t[1]:
        move += 'D'
        s = s[0] + chr(ord(s[1]) - 1)

    print(move)
