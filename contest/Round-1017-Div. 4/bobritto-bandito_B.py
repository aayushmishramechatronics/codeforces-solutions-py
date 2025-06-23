import sys

def solve():

    n, m, l, r = map(int, sys.stdin.readline().split())
    
    total_left_steps = -l
    total_right_steps = r
    
    if total_left_steps + total_right_steps == 0:  
        left_step = m // 2
    else:
        left_step = int(m * total_left_steps / (total_left_steps + total_right_steps))
    
    right_step = m - left_step
    
    l_prime = -left_step
    r_prime = right_step
    
    print(l_prime, r_prime)

t = int(sys.stdin.readline())
for _ in range(t):
    solve()
