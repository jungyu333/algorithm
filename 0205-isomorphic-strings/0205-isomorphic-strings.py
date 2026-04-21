class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        idx_s = []
        idx_t = []

        for s_char in s:
            idx_s.append(s.index(s_char))

            
        for t_char in t:
            idx_t.append(t.index(t_char))

        return idx_s == idx_t