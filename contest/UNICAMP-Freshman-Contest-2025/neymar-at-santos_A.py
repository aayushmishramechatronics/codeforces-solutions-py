t = int(input())  
s = int(input()) 
n = int(input()) 
r = int(input())  

max_per_teacher = min(s, n * r)

total_money = t * max_per_teacher

print(total_money)
