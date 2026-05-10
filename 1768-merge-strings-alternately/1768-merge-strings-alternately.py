class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merge = ''

        for w1, w2 in zip(word1, word2):
            merge += w1
            merge += w2
        
        n = min(len(word1), len(word2))

        merge += word1[n:]
        merge += word2[n:]

        return merge