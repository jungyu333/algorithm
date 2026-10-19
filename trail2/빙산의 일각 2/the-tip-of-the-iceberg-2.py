n = int(input())
h = [int(input()) for _ in range(n)]

MAX_H = max(h)

max_val = float('-inf')

# Please write your code here.

for height in range(MAX_H):

    prev = 0
    count = 0

    for item in h:
        diff = item - height if item >= height else 0

        if diff != 0 and prev == 0:   # 조각 시작
            count += 1

        prev = diff

    max_val = max(max_val, count)

        
    
print(max_val)