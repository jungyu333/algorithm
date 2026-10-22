n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

min_val = float('inf')

for i in range(n):
    arr[i] *= 2

    for j in range(n):
        remain = []

        for k in range(n):

            if j != k :
                remain.append(arr[k])
        
        diff = 0

        for k in range(len(remain) - 1):
            
            diff += abs(remain[k] - remain[k + 1])
        

        min_val = min(min_val, diff)    

    arr[i] //= 2

print(min_val)
