class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        sorted_strs = sorted(strs, reverse=False)
        
        prefix = ''

        for c1, c2 in zip(sorted_strs[0], sorted_strs[-1]):

            if c1 == c2:
                prefix += c1
            else:
                return prefix
        
        return prefix
        