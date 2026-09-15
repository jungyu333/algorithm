n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

offset = 100 * 1000

cnt_b = [0] * (2 * offset + 1)
cnt_w = [0] * (2 * offset + 1)
checked = [0] * (2 * offset + 1)

b, w, g = 0, 0, 0

current = offset

for distance, di in zip(x, dir):

    # 오른쪽
    if di == 'R':
        
        while distance > 0:

            checked[current] = 2
            cnt_b[current] += 1

            distance -= 1

            if distance:
                current += 1

    else:
        
        while distance > 0:

            checked[current] = 1
            cnt_w[current] += 1

            distance -= 1

            if distance:
                current -= 1

for i in range(2 * offset + 1):

    if cnt_b[i] >= 2 and cnt_w[i] >= 2:
        g += 1
    
    elif checked[i] == 1:
        w += 1
    elif checked[i] == 2:
        b += 1


print(w, b, g)