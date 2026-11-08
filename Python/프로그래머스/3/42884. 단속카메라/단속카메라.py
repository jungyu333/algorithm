def solution(routes):
    answer = 0
    
    routes = sorted(routes, key= lambda x:x[1])
    
    camera = routes[0][1]
    
    for route in routes:
        
        start, end = route
        
        if start <= camera <= end:
            continue
        else:
            camera = end
            answer += 1
    
    
    return answer + 1