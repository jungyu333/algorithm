N = int(input())
str = input()

# Please write your code here.

result = 0

for l in range(1, 101):
    
    history = {}

    for i in range(0, len(str) - l + 1):
        sub_str = str[i:i + l]

        if sub_str in history:
            history[sub_str] += 1
        else:
            history[sub_str] = 1

    if all(value == 1 for value in history.values()):
        result = l
        break
        
print(result)


    
       