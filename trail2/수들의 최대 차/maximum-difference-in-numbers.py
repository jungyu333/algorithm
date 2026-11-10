N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# Please write your code here.

max_val = float('-inf')

for m in range(1, 10001):

    num_list = []
    for n in arr:
        if m <= n <= m + K:
            num_list.append(n)
    
    max_val = max(max_val, len(num_list))

print(max_val)

