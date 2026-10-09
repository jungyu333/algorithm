n = int(input())
arr = [int(input()) for _ in range(n)]

# Please write your code here.

max_val = -1

def check_carries_three(num1, num2, num3):
    # 세 숫자를 문자열로 바꾸고 뒤집음 (일의 자리부터 계산)
    str1, str2, str3 = str(num1)[::-1], str(num2)[::-1], str(num3)[::-1]
    max_len = max(len(str1), len(str2), len(str3))
    
    carry = 0
    results = []
    
    for i in range(max_len):
        digit1 = int(str1[i]) if i < len(str1) else 0
        digit2 = int(str2[i]) if i < len(str2) else 0
        digit3 = int(str3[i]) if i < len(str3) else 0
        
        # 현재 자릿수 숫자 3개와 이전 carry의 총합
        current_sum = digit1 + digit2 + digit3 + carry
        
        if current_sum >= 10:
            # Carry 발생 -> True
            return True
        else:
            # Carry 미발생 -> False
            carry = 0
    
    return False

for i in range(n-2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):

            if(check_carries_three(arr[i], arr[j], arr[k]) is False):

                max_val = max(max_val , arr[i] + arr[j] + arr[k])


print(max_val)