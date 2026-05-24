class Solution:
    def simplifyPath(self, path: str) -> str:
        splited_path = path.split("/")

        stack = []

        for token in splited_path:
            
            if token == '..' and stack:
                stack.pop()
            elif token != '' and token != '.' and token != '..':
                stack.append(token)

        return '/' + '/'.join(stack)