from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        idx_arr = []

        for char in s:
            idx_arr.append(s.index(char))
        
        counters = Counter(idx_arr)

        uniques = []

        for key, value in counters.items():
            if value == 1:
                uniques.append(key)
        
        return min(uniques) if uniques else -1