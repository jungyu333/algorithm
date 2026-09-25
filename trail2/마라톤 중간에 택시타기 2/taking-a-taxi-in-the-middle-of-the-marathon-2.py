n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.

def calc(start, destination):

    return abs(start[0] - destination[0]) + abs(start[1] - destination[1])


answer = float('inf')

for skip in range(1, n - 1):
    route = points[:skip] + points[skip + 1:]
    
    total = 0
    for i in range(len(route) - 1):
        total += calc(route[i], route[i + 1])

    answer = min(answer, total)

print(answer)