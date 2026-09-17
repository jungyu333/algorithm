n = int(input())
A = list(map(int, input().split()))

# Please write your code here.

import sys

MAX = sys.maxsize

min_val = MAX

for i in range(n):

    sum_distance = 0

    for j in range(n):

        sum_distance += A[j] * abs(i - j)

    min_val = min(min_val, sum_distance)

print(min_val)
