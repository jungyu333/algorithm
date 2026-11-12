N = int(input())
seat = input()

# Please write your code here.


def get_possiable_seat(N, seat):
    is_possiable_seat = []
    seat = list(seat)

    for i in range(N):
        if seat[i] == '0':
            is_possiable_seat.append(i)
    
    return is_possiable_seat

is_possiable_seat = get_possiable_seat(N, seat)

def get_min_distance(s1, s2, seat):

    min_distance = float('inf')
    seat = list(seat)
    seat[s1] = '1'
    seat[s2] = '1'

    people_index = []
    
    for i in range(len(seat)):
        if seat[i] == '1':
            people_index.append(i)

    
    for j in range(len(people_index) - 1):
        for k in range(j + 1, len(people_index)):

            dist = people_index[k] - people_index[j]

            min_distance = min(min_distance , dist)
    
    return min_distance

result = float('-inf')

for i in range(len(is_possiable_seat) - 1):
    for j in range(i + 1, len(is_possiable_seat)):

        min_distance = get_min_distance(is_possiable_seat[i], is_possiable_seat[j], seat)

        result = max(min_distance, result)

print(result)