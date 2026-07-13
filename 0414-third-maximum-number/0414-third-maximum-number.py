import heapq

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        heap = []

        for num in nums:

            if num in heap:
                continue
            
            if len(heap) < 3:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappushpop(heap, num)
        

        return heap[0] if len(heap) == 3 else max(heap)