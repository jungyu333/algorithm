import math

n = int(input())
a = [int(input()) for _ in range(n)]

# Please write your code here.

rooms = a + a

min_val = math.inf

for i in range(n):
    
    sum = 0
    
    for j in range(i, i + n):
        
        sum += rooms[j] * (j - i)
        
    min_val = min(min_val , sum)

print(min_val)
