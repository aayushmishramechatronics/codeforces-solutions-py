s = input()
s2 = ''
i = 0

while i < len(s):
    if s[i] == '.':
        s2 += '0'
        i += 1
    elif s[i] == '-' and i + 1 < len(s):
        if s[i + 1] == '.':
            s2 += '1'
        elif s[i + 1] == '-':
            s2 += '2'
        i += 2

print(s2)
