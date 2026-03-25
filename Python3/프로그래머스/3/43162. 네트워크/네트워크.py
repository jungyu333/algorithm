def solution(n, computers):
    answer = 0
    
    visited = [False] * n
    
    def DFS(i):
        
        visited[i] = True
        
        for j in range(n):
            
            if computers[i][j] == 1 and not visited[j]:
                DFS(j)
    
    for i in range(n):
        
        if not visited[i]:
            DFS(i)
            answer += 1
    
    return answer