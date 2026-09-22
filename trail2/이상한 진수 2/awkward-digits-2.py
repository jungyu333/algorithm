a = input()

# Please write your code here.

candidate = []

max_val = 0

binary = list(map(int, a))
cnt = len(binary)

for i in range(cnt):

    binary[i] = (binary[i]+1)%2

    candidate.append(binary[:])


    binary[i] = (binary[i]+1)%2


for can in candidate:

    temp = ''
    for ch in can:
        temp += str(ch)
    
    max_val = max(max_val, int(temp, 2))

print(max_val)