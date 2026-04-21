from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hash = Counter(magazine)
        
        for char in ransomNote:

            if not hash.get(char):
                return False

            if hash.get(char) == 0:
                return False            

            hash[char] -= 1
        
        return True