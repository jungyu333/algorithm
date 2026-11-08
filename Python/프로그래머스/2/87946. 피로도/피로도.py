from itertools import permutations

def solution(k, dungeons):


    max_count = 0

    
    for order in permutations(dungeons, len(dungeons)):
        
        current_k = k
        count = 0
        for dungeon in order:
            
            require , consume = dungeon[0], dungeon[1]
            
            if current_k >= require:
                current_k -= consume
                count += 1
            else:
                break
        
        max_count = max(max_count , count)
        

        
    return max_count