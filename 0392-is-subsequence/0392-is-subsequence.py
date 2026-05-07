class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        start = 0
        count = 0

        for idx in range(0, len(s)):
            
            for j in range(start, len(t)):
                if s[idx] == t[j]:
                    start = j + 1
                    count += 1
                    break

        return count == len(s)