class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        for char in s:
            
            if char in ['(', '{', '[']:
                stack.append(char)
            else:
                if not stack or not stack[-1]:
                    return False
                else:
                    if stack[-1] == '(' and char == ')':
                        stack.pop()
                    elif stack[-1] == '{' and char == '}':
                        stack.pop()
                    elif stack[-1] == '[' and char == ']':
                        stack.pop()
                    else:
                        return False

        return True if not stack else False