from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hash_m = Counter(magazine)
        hash_r = Counter(ransomNote)
        
        hash = hash_r - hash_m

        return not hash