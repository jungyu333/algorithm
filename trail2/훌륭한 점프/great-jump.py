n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.

max_a = max(arr)

def is_possible(stone_num, stons):

    possible_stone = []

    for i, elem in enumerate(stons):
        if elem <= stone_num:
            possible_stone.append(i)
    
    arr_size = len(possible_stone)
    for i in range(1, arr_size):
        dist = possible_stone[i] - possible_stone[i - 1]
        if dist > k:
            return False
    
    return True

max_min = float('-inf')

for a in range(max(arr[0], arr[-1]), max_a + 1):

    if is_possible(a, arr):
        max_min = a
        break

print(max_min)