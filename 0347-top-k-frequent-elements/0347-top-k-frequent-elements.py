from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        counters = Counter(nums)

        heap = [ (-val, key) for key, val in counters.items()]
        
        heapq.heapify(heap)

        for i in range(k):
            val, key = heapq.heappop(heap)

            result.append(key)
        
        return result
        