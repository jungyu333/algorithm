from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        queue = deque([(root, 1)])

        while queue:

            if not root:
                return 0

            pop = queue.popleft()

            if pop[0].left is None and pop[0].right is None:
                return pop[1]
            
            if pop[0].left:
                queue.append([pop[0].left, pop[1] + 1])
            
            if pop[0].right:
                queue.append([pop[0].right, pop[1] + 1])

        