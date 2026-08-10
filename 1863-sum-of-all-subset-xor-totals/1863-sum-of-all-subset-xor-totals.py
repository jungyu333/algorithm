from itertools import combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0
        def backtrack(index, xor):
            nonlocal result 

            if index == len(nums):

                result += xor
                return
            
            backtrack(index + 1, xor ^ nums[index])
            backtrack(index + 1, xor)


        backtrack(0, 0)

        return result
                