N = int(input())
heights = [int(input()) for _ in range(N)]

# Please write your code here.

min_val = float('inf')

for l in range(1, 84):
    
    min_height = l
    max_height = l + 17

    cost = 0

    for h in heights:
        if h < min_height:
            diff = min_height - h

            cost += diff * diff
        
        elif h > max_height:
            diff = h - max_height

            cost += diff * diff
    
    min_val = min(min_val, cost)


print(min_val)