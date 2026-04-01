class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        index = 0

        while index < len(nums):

            if nums[index] == val:
                nums.pop(index)
                
                if index >= 1:
                    index -= 1
                else:
                    index = 0
                
            else:
                index += 1


        return len(nums)