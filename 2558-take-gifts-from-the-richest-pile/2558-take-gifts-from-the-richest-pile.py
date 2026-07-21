import heapq

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        heap = [-gift for gift in gifts]
        
        heapq.heapify(heap)

        for i in range(k):

            max_val = heapq.heappop(heap)

            heapq.heappush(heap, -math.floor(math.sqrt(-max_val)))

        return -sum(heap)