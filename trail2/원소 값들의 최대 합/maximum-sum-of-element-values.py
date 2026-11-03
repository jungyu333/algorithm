n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

# Please write your code here.

max_val = float('-inf')

for start in range(1, n+1):
    
    sum_value = 0
    current = start
    for count in range(m):
        
        next_pointer = arr[current]
        sum_value += next_pointer
        current = next_pointer
    
    max_val = max(max_val, sum_value)

print(max_val)