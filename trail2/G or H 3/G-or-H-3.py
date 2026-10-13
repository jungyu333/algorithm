n, k = map(int, input().split())
x = []
c = []
for _ in range(n):
    pos, char = input().split()
    x.append(int(pos))
    c.append(char)

# Please write your code here.
max_num = 10000
temp = [0] * (max_num + 1)

max_val = float('-inf')

for position, char in zip(x, c) :
    
    if char == 'G':
        temp[position] = 1
    elif char == 'H':
        temp[position] = 2


for i in range(max_num - k + 1):
    
    current = 0

    for j in range(i, i + k + 1):
        
        current += temp[j]
    
    max_val = max(max_val, current)
        
print(max_val)