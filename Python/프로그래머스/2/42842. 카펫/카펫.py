def solution(brown, yellow):
    answer = []
    
    divide = []
    
    for i in range(yellow, 0, -1):
        
        if yellow % i == 0 and i >= yellow // i:
            divide.append((i , yellow // i))
    
    
    
    for div in divide:
        yellow_w , yellow_h = div
        
        brown_w = yellow_w * 2
        brown_h = yellow_h * 2
        
        remain_brown_block = brown - (brown_w + brown_h)
        
        if remain_brown_block == 4:
            answer = [yellow_w + 2, yellow_h + 2]
            break
    
    return answer