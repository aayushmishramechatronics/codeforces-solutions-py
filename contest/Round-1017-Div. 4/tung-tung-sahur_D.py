def compress(s):
    groups = []
    if not s:
        return groups

    cur = s[0]
    count = 1
    for ch in s[1:]:
        if ch == cur:
            count += 1
        else:
            groups.append((cur, count))
            cur = ch
            count = 1
    groups.append((cur, count))
    return groups

t = int(input())
for _ in range(t):
    p = input().strip()
    s = input().strip()

    if len(s) < len(p) or len(s) > 2 * len(p):
        print("NO")
        continue

    gp = compress(p)
    gs = compress(s)

    if len(gp) != len(gs):
        print("NO")
        continue

    ok = True
    for (cp, np), (cs, ns) in zip(gp, gs):
        if cp != cs or ns < np or ns > 2 * np:
            ok = False
            break

    print("YES" if ok else "NO")
