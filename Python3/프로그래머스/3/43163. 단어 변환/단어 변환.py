from collections import deque

def helper(current, next):
    
    count = 0
    
    for c , n in zip(current, next):
        if c != n:
            count += 1
    
    return count == 1


def solution(begin, target, words):
    answer = 0
    
    queue = deque([(begin, 0)])
    
    while queue:
        
        current, depth = queue.popleft()
        
        if current == target:
            answer = depth
            break
        
        for word in words:
            
            # 1개만 바꿔서 바꿀수 있으면
            if helper(current, word):
                
                queue.append((word, depth + 1))
                words.remove(word)
    
    return answer