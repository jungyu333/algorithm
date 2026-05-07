class Solution:
    def reverseWords(self, s: str) -> str:
        
        words = s.split(' ')

        def reverse_helper(word):
            splited = list(word)
            start = 0
            end = len(splited) - 1
            
            while start < end :
                splited[end], splited[start] = splited[start], splited[end]
                start += 1
                end -= 1

            
            return ''.join(splited)
        
        reverse_words = list(map(reverse_helper, words))

        return ' '.join(reverse_words)