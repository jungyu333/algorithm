import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heap = [-item for item in stones]

        heapq.heapify(heap)

        while len(heap) > 1:

            stone_a = -heapq.heappop(heap)
            stone_b = -heapq.heappop(heap)

            if stone_a != stone_b:
                diff = stone_a - stone_b
                heapq.heappush(heap, -diff)
            
        

        return -heap[0] if len(heap) else 0