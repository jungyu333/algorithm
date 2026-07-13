import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        heap = [(-s, i) for i, s in enumerate(score)]
        heapq.heapify(heap)
        rank = 1
        while heap:
            s, index = heapq.heappop(heap)
            if rank == 1:
                score[index] = 'Gold Medal'
            elif rank == 2:
                score[index] = 'Silver Medal'
            elif rank == 3:
                score[index] = 'Bronze Medal'
            else:
                score[index] = str(rank)
            
            rank += 1

        return score