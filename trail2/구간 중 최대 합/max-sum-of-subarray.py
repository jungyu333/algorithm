n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

max_val = float('-inf')

for i in range(n - k + 1):
    
    current_sum = 0
    
    for j in range(i, i + k):

        current_sum += arr[j]
    
    max_val = max(max_val, current_sum)

print(max_val)