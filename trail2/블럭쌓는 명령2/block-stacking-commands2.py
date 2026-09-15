n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

paints = [0] * (n + 1)

for command in commands:

    start, end = command[0], command[1]

    for i in range(start, end + 1):

        paints[i] += 1


print(max(paints))