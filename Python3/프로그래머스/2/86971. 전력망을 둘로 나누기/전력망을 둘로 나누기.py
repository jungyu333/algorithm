from collections import deque


def solution(n, wires):
    answer = n
    
    tree = [[] for _ in range(n + 1) ]
    
    for a , b in wires:
        tree[a].append(b)
        tree[b].append(a)
    
    def bfs(start):
    
        visited = [0] * (n + 1)
        queue = deque([start])
        visited[start] = 1
        count = 1
        
        while queue:
            s = queue.popleft()
            for i in tree[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = 1
                    count += 1
        
        return count
                
    
    for a, b in wires:
        
        tree[a].remove(b)
        tree[b].remove(a)
        
        
        left = bfs(a)
        right = bfs(b)
        
        abs_value = min(abs(left - right), answer)
      
        answer = abs_value
        
        tree[a].append(b)
        tree[b].append(a)
    
    
    
    return answer