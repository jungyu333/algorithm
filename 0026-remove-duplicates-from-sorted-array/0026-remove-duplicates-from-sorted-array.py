class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        current = 0
        next = 1

        while True:

            if current == len(nums) - 1:
                break
            
            # 중복된 경우
            if nums[current] == nums[next]:
                nums.pop(next)
               

            # 중복 되지 않은 경우
            elif nums[current] != nums[next]:
                current += 1
                next += 1