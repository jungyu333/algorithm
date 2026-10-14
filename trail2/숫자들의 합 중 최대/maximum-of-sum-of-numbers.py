X, Y = map(int, input().split())

# Please write your code here.

max_val = float('-inf')

for number in range(X, Y+1):

    digit_list = list(map(int, str(number)))
    
    max_val = max(max_val, sum(digit_list))

print(max_val)