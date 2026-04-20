from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hash_s = Counter(s)
        hash_t = Counter(t)

        for ch_s, ch_t in zip(s, t):
            
            if not hash_t.get(ch_s):
                return False
            
            if not hash_s.get(ch_t):
                return False
            

            if hash_t.get(ch_s):
                hash_t[ch_s] -= 1
            
            if hash_s.get(ch_t):
                hash_s[ch_t] -= 1
            
            
        return True