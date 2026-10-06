A = input()

# Please write your code here.

result = 0

for i in range(len(A) - 2):

    for j in range(i + 2, len(A) - 1):

        if (A[i] +  A[i + 1] == '((') and (A[j] + A[j + 1] == '))'):

            result += 1

print(result)