n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

paints = [0] * 101

for seg in segments:

    start, end = seg[0], seg[1]


    for i in range(start, end + 1):
        paints[i] += 1


print(max(paints))