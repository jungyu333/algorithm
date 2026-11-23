N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# Please write your code here.

exploded = [False] * N          

for i in range(len(num) - 1):

    current = num[i]

    for j in range(i + 1, len(num)):

        next_num = num[j]

        if j - i <= K and current == next_num:
            exploded[i] = True  
            exploded[j] = True 

bomb_count_map = {}

for i in range(N):             
    if exploded[i]:
        bomb_count_map[num[i]] = bomb_count_map.get(num[i], 0) + 1

max_val = max(bomb_count_map, key=lambda k: (bomb_count_map[k], k), default = 0)

print(max_val)