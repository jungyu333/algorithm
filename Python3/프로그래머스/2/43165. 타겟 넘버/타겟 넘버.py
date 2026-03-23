

def solution(numbers, target):
    answer = 0
    
    stack = [(0, 0)]
    
    while stack:
        
        index, current_sum = stack.pop()
        
        if index == len(numbers):
            
            if target == current_sum:
                answer += 1
            continue
        
        stack.append((index + 1, current_sum + numbers[index]))
        stack.append((index + 1, current_sum - numbers[index]))
    
    return answer