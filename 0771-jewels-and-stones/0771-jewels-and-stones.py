from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        result = 0

        stone = Counter(stones)
        
        for key, value in stone.items():

            if key in jewels:
                result += value
        
        return result