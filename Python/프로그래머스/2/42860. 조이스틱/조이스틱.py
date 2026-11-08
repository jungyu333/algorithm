def solution(name):
    answer = 0
    
    length = len(name)
    
    up_down = 0
    
    min_move = length - 1
    
    for i, n in enumerate(name):
        up_down += min([ord(n) - ord("A"), ord("Z")- ord(n) + 1])     
        next = i + 1
        
        while next < length and name[next] == "A":
            next += 1
        
        right = 2 * i + length - next
        reverse = 2 * (length - next) + i
        min_move = min([min_move, right, reverse])
        
    answer = min_move + up_down
    
    return answer