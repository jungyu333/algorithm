N, C, G, H = map(int, input().split())
ranges = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.

MAXIMUM = 3000
max_val = float('-inf')

def get_temperature(value, temp):

    start, end = temp[0], temp[1]

    if value < start:
        return C
    elif start <= value <= end:
        return G
    elif value > end:
        return H

for t in range(-MAXIMUM, MAXIMUM):

    current = 0
    for device in ranges:
        device_t = get_temperature(t, device)
        
        current += device_t
    
    max_val = max(max_val, current)
    

print(max_val)