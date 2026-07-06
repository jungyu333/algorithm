class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        count = 0

        for row in grid:

            start = 0
            end = len(row) - 1

            while start <= end :
                mid = (start + end) // 2

                if row[mid] >= 0:
                    start = mid + 1
                elif row[mid] < 0:
                    end = mid - 1
            
            count += len(row) - start
              

        return count