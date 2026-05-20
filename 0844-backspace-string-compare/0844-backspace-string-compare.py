class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(string):
            stack = []

            for char in string:

                if char == '#':

                    if stack:
                        stack.pop()

                else:
                    stack.append(char)
            
            return ''.join(stack)

        result_s = helper(s)
        result_t = helper(t)

        return result_s == result_t