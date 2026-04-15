class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        temp = []

        for sentence in sentences:
            splited = sentence.split(' ')
            temp.append(len(splited))
        
        return max(temp)