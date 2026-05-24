class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        depth = 0
        stack = []

        for char in s :

            if char == '(':
                depth += 1

                if depth > 1:
                    stack.append(char)


            else:
                depth -= 1

                if depth > 0:
                    stack.append(char)

        return ''.join(stack)