import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        transform = ''

        s = re.sub(r'[^a-z0-9]', '', s.lower())

        start = 0
        end = len(s) - 1

        while start < end :
            
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        
        return True