import sys
input = sys.stdin.readline

def count_winning_triples(a):
    n = len(a)
    M = a[-1]
    cnt = 0
    for k in range(2, n):
        z = a[k]
        thresh = z if z >= M - z else M - z

        i, j = 0, k - 1
        while i < j:
            if a[i] + a[j] > thresh:
                cnt += (j - i)
                j -= 1
            else:
                i += 1

    return cnt

def main():
    t = int(input())
    out = []
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        out.append(str(count_winning_triples(a)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
