n = int(input())
a = list(map(int, input().split()))

# Please write your code here.

max_val = float('-inf')

MAX_K = max(a)
for k in range(0, MAX_K):
    
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            
            if (a[j] - k) == (k - a[i]):
                count += 1

    max_val = max(max_val, count)

print(max_val)