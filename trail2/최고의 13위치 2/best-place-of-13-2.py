n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

max_val = 0

for i1 in range (n):
    for j1 in range(n - 2):
        for i2 in range(n):
            for j2 in range(n - 2):

                if i1 == i2 and abs(j1 - j2) < 3:
                    continue
                else:
                    sum = arr[i1][j1] + arr[i1][j1+1] + arr[i1][j1+2] + arr[i2][j2] + arr[i2][j2+1] + arr[i2][j2+2]

                    max_val = max(max_val , sum)

print(max_val)