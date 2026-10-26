n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.

unique_x = list(set(x))
unique_y = list(set(y))

line_list = []
# print(points)
for i in unique_x:

    line_list.append(('x', i))

for i in unique_y:

    line_list.append(('y', i))

result = 0

if len(line_list) <= 3:
    result = 1

for i in range(len(line_list)-2):
    for j in range(i + 1, len(line_list)-1):
        for k in range(j + 1, len(line_list)):
            
            line_a, line_b, line_c = line_list[i], line_list[j], line_list[k]
            
            loop = [line_a, line_b, line_c]
            
            copy_points = points.copy()
            for axis, value in loop:
                if axis == 'x':
                    copy_points = [p for p in copy_points if p[0] != value]
                else:
                    copy_points = [p for p in copy_points if p[1] != value]

                if len(copy_points) == 0:
                    result = 1
                    break

print(result)