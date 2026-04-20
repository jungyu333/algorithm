class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = {}
                
        for i in range(len(nums)):
            
            if hash.get(target - nums[i]) != None and hash.get(target - nums[i]) != i:

                return [i, hash.get(target-nums[i])]
            
            hash[nums[i]] = i