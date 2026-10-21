n = int(input())
moves = [tuple(map(int, input().split())) for _ in range(n)]
a, b, c = zip(*moves)
a, b, c = list(a), list(b), list(c)



# Please write your code here.

cases = []
max_val = float('-inf')

def helper(position, a, b, c):

    position[b], position[a] = position[a], position[b] 

    if position[c] == 1:
        return 1
    
    return 0

for i in range(n):
    cases.append([a[i], b[i], c[i]])


for i in range(1, 4):
    position = [0, 0, 0, 0]
    position[i] = 1
    result = 0
    for case in cases:
        
        a, b, c = case[0], case[1], case[2]
        
        point = helper(position, a, b, c)

        result += point
    
    max_val = max(max_val, result)

print(max_val)
    