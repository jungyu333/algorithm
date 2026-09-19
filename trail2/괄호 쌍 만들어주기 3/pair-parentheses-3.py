A = input()

# Please write your code here.

result = 0

for i in range(len(A) - 1):

    for j in range(i + 1, len(A)):
        
        if A[i] == '(' and A[j] == ')':

            result += 1


print(result)
