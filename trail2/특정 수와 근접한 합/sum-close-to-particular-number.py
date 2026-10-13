N, S = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

min_val = float('inf')

sum_val = sum(arr)

for i in range(N - 1):
    for j in range(i + 1, N):

        t = (sum_val - (arr[i] + arr[j]))
        
        min_val = min(min_val, abs(S - t))

        if min_val == 0:
            break

print(min_val)