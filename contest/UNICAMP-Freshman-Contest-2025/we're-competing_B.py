K = int(input())
S = input()
target = "tamocompetindo"
p = len(S)
r = len(target)

found = False

for i in range(p - r + 1):
    segment = S[i:i + r]

    diff = sum(1 for a, b in zip(segment, target) if a != b)
    if diff <= K:
        found = True
        break

print("SIM" if found else "NAO")
