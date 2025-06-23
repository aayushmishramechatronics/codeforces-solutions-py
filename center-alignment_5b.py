v = []

while True:
    try:
        s = input()
    except EOFError:
        break
    l = len(s)
    v.append([s, l])


vm = v[:]
vm.sort(key=lambda x: x[1])
width = vm[-1][1] + 2

cc = 0
print('*' * width)


for i in range(len(v)):
    temp = v[i]

    
    if (width - temp[1]) % 2:
        if cc % 2 == 0:
            temp[0] += ' '
        else:
            temp[0] = ' ' + temp[0]
        temp[1] += 1
        cc += 1

    sw = (width - temp[1]) // 2
    lw = '*' + ' ' * (sw - 1)
    rw = ' ' * (sw - 1) + '*'
    temp[0] = lw + temp[0] + rw
    print(temp[0])

print('*' * width)
