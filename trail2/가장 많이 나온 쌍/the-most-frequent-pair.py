n, m = map(int, input().split())
pairs = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

hash = {}

for x, y in pairs:

    temp = tuple(sorted([x, y]))
    
    if temp in hash:
        hash[temp] += 1
    else:
        hash[temp] = 1
    
print(max(hash.values()))