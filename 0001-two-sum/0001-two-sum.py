class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}

        for i in range(len(nums)):
            hash[nums[i]] = i
        
        for i in range(len(nums)):

            if hash.get(target - nums[i]) and hash.get(target - nums[i]) != i:

                return [i, hash.get(target-nums[i])]