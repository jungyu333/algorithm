def solution(n, costs):
    answer = 0
    
    costs = sorted(costs, key = lambda x: x[2])
    
    islands = {costs[0][0]}
    
    while len(islands) < n :
        
        for i in range(len(costs)):
            
            start, end, edge_cost = costs[i]
            
            if start in islands and end in islands:
                continue
            
            
            elif start in islands or end in islands:
                islands.add(start)
                islands.add(end)
                answer += edge_cost
                costs.remove(costs[i])
                break

                
    
    
    return answer