
def solution(number, k):
    answer = ''
    
    stack = []
    i = 0
    
    while i < len(number):
        num = number[i]
        
        while k > 0 and stack and stack[-1] < num:
            stack.pop()
            k -= 1
            
        stack.append(num)
        i += 1

        
    if k > 0:
        stack = stack[:-k]

    answer = ''.join(stack)
    
    return answer