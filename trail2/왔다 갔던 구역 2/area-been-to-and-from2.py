n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Please write your code here.

length = 2101

paints = [0] * length

current = length // 2

for count , di in zip(x, dir):
    
    if di == 'R':
        for i in range(current, current + count):
            paints[i] += 1
            
        current += count
        
    
    else:
        for i in range(current - count, current):
            paints[i] += 1
        
        current -= count
        

result = 0

for c in paints:

    if c >= 2:
        result += 1

print(result)
    
