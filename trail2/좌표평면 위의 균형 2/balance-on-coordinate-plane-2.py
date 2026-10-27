n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

min_val = float('inf')

for row in range(2, 100, 2):
    
    for col in range(2, 100, 2):

        area_1 = []
        area_2 = []
        area_3 = []
        area_4 = []

        for point in points:

            x, y = point[0], point[1]

            # 1사분면
            if x >= col and y >= row:
                area_1.append(point)
            # 2사분면
            elif x <= col and y >= row:
                area_2.append(point)
            # 3사분면
            elif x <= col and y <= row:
                area_3.append(point)
            # 4사분면
            else:
                area_4.append(point)

        M = max(len(area_1), len(area_2), len(area_3), len(area_4))
        
        min_val = min(min_val, M)

print(min_val)