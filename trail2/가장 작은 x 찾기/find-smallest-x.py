n = int(input())
ranges = [tuple(map(int, input().split())) for _ in range(n)]
a, b = zip(*ranges)
a, b = list(a), list(b)

# Please write your code here.

result = 0

for i in range(1, 10001):
    count = 0
    for N in range(1, n + 1):
        
        if a[N - 1] <= i * (2 ** N) <= b[N - 1]:
            
            count += 1

    if count == n:
        result = i
        break

print(result)