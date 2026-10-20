X, Y = map(int, input().split())

# Please write your code here.

result = 0

def is_palindrome(number):

    str_number = str(number)
    num_len = len(str_number)
    middle = num_len // 2

    if num_len % 2 == 0:
        return str_number[:middle] == str_number[middle:][::-1]
    else:
        return str_number[:middle] == str_number[middle+1:][::-1]

for n in range(X, Y + 1):

    if is_palindrome(n):
        result += 1

print(result)