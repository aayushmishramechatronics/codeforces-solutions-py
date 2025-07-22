import sys
def solve():
    MOD = 998244353
    def power(base, exp):
        res = 1
        base %= MOD
        while exp > 0:
            if exp % 2 == 1:
                res = (res * base) % MOD
            base = (base * base) % MOD
            exp //= 2
        return res

    def mod_inverse(n):
        return power(n, MOD - 2)

    input = sys.stdin.readline
    n, m = map(int, input().split())

    segs_by_r = [[] for _ in range(m + 1)]
    total_prob_none = 1
    
    for _ in range(n):
        l, r, p, q = map(int, input().split())
        prob_not_exist = ((q - p) * mod_inverse(q)) % MOD
        total_prob_none = (total_prob_none * prob_not_exist) % MOD
        weight = (p * mod_inverse(q - p)) % MOD
        segs_by_r[r].append((l, weight))

    dp = [0] * (m + 1)
    dp[0] = 1

    for i in range(1, m + 1):
        current_dp_val = 0
        for l_seg, w_seg in segs_by_r[i]:
            current_dp_val = (current_dp_val + w_seg * dp[l_seg - 1]) % MOD
        dp[i] = current_dp_val
        
    final_answer = (dp[m] * total_prob_none) % MOD
    print(final_answer)

solve()
