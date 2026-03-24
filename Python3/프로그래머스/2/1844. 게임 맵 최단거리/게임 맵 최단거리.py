from collections import deque

def solution(maps):
    answer = 0
    
    q = deque([(0, 0)])
    
    # 상 하 좌 우
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    n = len(maps)
    m = len(maps[0])
    
    while q :
        current = q.popleft()
        y, x = current
        
        for di in direction:
            
            next_y = y + di[0]
            next_x = x + di[1]
            
            if 0 <= next_y < n and 0 <= next_x < m and maps[next_y][next_x] == 1:
                maps[next_y][next_x] = maps[y][x] + 1
                q.append((next_y, next_x))
                
                
    if maps[n - 1][m - 1] != 1:
        answer = maps[n - 1][m - 1]
    else:
        answer = -1
    
    return answer