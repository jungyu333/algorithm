import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = re.sub(r'[^a-z0-9]', '', s.lower())

        s_reverse = ''.join(reversed(s))
        
        return s == s_reverse