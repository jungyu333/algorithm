class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        current = 0

        for next in range(1, len(nums)):
            if nums[current] != nums[next]:
                current += 1
                nums[current] = nums[next] 
        
        return current + 1