class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        idx_1 = 0
        idx_2 = 0

        merge = ''

        while idx_1 < len(word1) and idx_2 < len(word2):
            
            merge += word1[idx_1]
            merge += word2[idx_2]
        
            idx_1 += 1
            idx_2 += 1

        
        if idx_1 == len(word1):
            merge += word2[idx_2:]
        
        if idx_2 == len(word2):
            merge += word1[idx_1:]
        
        return merge