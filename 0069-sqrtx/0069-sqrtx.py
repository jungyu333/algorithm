class Solution:
    def mySqrt(self, x: int) -> int:
        
        start = 1
        end = x

        while start <= end:

            mid = (start + end) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                end = mid - 1
            else:
                start = mid + 1
        
        return start - 1