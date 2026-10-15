T, a, b = map(int, input().split())
c = []
x = []
for _ in range(T):
    char, pos = input().split()
    c.append(char)
    x.append(int(pos))

# Please write your code here.

position = [0] * 1001

for char, i in zip(c, x):
    position[i] = char

def get_min_distance(target, current):

    min_val = float('inf')

    for char, i in zip(c, x):
        if char == target:
            distance = abs(current - i)
            min_val = min(distance, min_val)
    
    return min_val

result = 0

for k in range(a, b + 1):
    
    min_dis_s = get_min_distance('S', k)
    min_dis_n = get_min_distance('N', k)
    
    if min_dis_s <= min_dis_n:
        result += 1

print(result)