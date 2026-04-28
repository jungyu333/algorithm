class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = len(nums) - 1
        idx = len(nums) - 1
        result = [0] * len(nums)

        while left <= right :

            if nums[left]**2 < nums[right]**2:
                result[idx] = nums[right]**2
                right -= 1
            else:
                result[idx] = nums[left]**2
                left += 1
            
            idx -= 1
        
        return result