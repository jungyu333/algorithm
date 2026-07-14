import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        heap = [(sum(row), i) for i , row in enumerate(mat)]

        heapq.heapify(heap)

        answer = []

        for i in range(k):

            answer.append(heapq.heappop(heap)[1])

        return answer
