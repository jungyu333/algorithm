N = int(input())
seat = input()

# Please write your code here.

people = []

max_val = float('-inf')

for i in range(N):
    
    if seat[i] == '1':
        people.append(i)

for i in range(N):
    
    if seat[i] != '1':
        
        distance = []

        position = sorted(people + [i])

        for j in range(len(position) - 1):

            distance.append(position[j + 1] - position[j])
            
        min_distance = min(distance)

        max_val = max(max_val, min_distance)

print(max_val)