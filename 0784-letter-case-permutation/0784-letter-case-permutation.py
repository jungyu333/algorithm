class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        
        result = []

        def backtrack(index, path):

            if index == len(s):
                result.append(path)
                return
            
            char = s[index]

            if char.isalpha():
                backtrack(index + 1, path + char.lower())
                backtrack(index + 1, path + char.upper())
            else:
                backtrack(index + 1, path + char)
        
        backtrack(0, '')

        return result