class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        splited = s.split(' ')

        return [ pattern.index(p) for p in pattern ] == [ splited.index(s) for s in splited] 

