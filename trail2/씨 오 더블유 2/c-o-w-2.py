n = int(input())
S = input()

# Please write your code here.

count = 0

for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if S[i] + S[j] + S[k] == 'COW':
                count += 1 

print(count)