class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        result = []

        sorted_nums = sorted(nums)

        for num in nums:
            count = sorted_nums.index(num)
            result.append(count)

        return result