from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        result = []

        counters = Counter(words)

        heap = [(-val, key) for key, val in counters.items()]

        heapq.heapify(heap)

        for i in range(k) :
            item = heapq.heappop(heap)

            result.append(item[1])
        
        return result