from itertools import accumulate

class NumArray:

    def __init__(self, nums: List[int]):
        self._prefix = [0] + list(accumulate(nums))


    def sumRange(self, left: int, right: int) -> int:
        
        result = 0

        result = self._prefix[right + 1] - self._prefix[left]
        
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)