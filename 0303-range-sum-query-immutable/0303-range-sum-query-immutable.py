class NumArray:

    def __init__(self, nums: List[int]):
        self._prefix = self.calc_prefix(nums)

    def calc_prefix(self, nums: List[int]):

        prefix_sums = []

        for num in nums:

            if not prefix_sums:
                prefix_sums.append(num)
            else:
                prefix_sums.append(prefix_sums[-1] + num)
        return prefix_sums

    def sumRange(self, left: int, right: int) -> int:
        
        result = 0

        if left == 0:
            result = self._prefix[right]
        else:
            result = self._prefix[right] - self._prefix[left - 1]
        
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)