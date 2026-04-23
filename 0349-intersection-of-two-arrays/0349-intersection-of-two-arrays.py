from collections import Counter

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        num1_set = list(set(nums1))
        num2_set = list(set(nums2))

        num1_counters = Counter(num1_set)

        result = []

        for num in num2_set:
            if num1_counters.get(num):
                result.append(num)
        
        return result