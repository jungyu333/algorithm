class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = [s[0]]

        s_list = list(s)

        for idx in range(1, len(s_list)):
            
            if not stack:
                stack.append(s_list[idx])

            else:
                top = stack[-1]
                if top == s_list[idx]:
                
                    stack.pop()

                else:

                    stack.append(s_list[idx])

        return ''.join(stack)