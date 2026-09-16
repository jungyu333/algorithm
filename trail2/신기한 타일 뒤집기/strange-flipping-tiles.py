n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Please write your code here.

offset = 100 * 1000

max = 2 * 100 * 1000

checked = [0] * (max + 1)

current = offset + 0

for distance, di in zip(x, dir):

    # 오른쪽 이동
    if di == 'R':

        for i in range(current, current + distance):
            checked[i] = 1
        
        current += (distance - 1)
        


    # 왼쪽 이동

    elif di == 'L':

        for i in range(current - distance + 1, current + 1):

            checked[i] = -1
        
        current -= (distance - 1)
        

white = 0
black = 0

for tile in checked:

    if tile == -1:

        white += 1
    
    elif tile == 1:

        black += 1


print(white, black)