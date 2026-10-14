from collections import Counter
X, Y = map(int, input().split())

# Please write your code here.

def is_interest_num(number):

    digit_list = list(map(int, str(number)))

    digit_count = Counter(digit_list)
    
    for key, value in digit_count.items():
        if value == 1 and len(digit_count) == 2:
            return True
    
    return False


result = 0

for num in range(X, Y + 1):
    
    if is_interest_num(num):
        result += 1

print(result)