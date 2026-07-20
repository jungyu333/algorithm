import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        heap = []
        result = []

        for point in points:
            x, y = point[0], point[1]
            distance = math.sqrt(x ** 2 + y ** 2)
            heap.append((distance , [x, y]))
        
        heapq.heapify(heap)

        for i in range(k):

            closest = heapq.heappop(heap)
            result.append(closest[1])


        return result