# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def DFS(node, remain):

            if not node:
                return False
            
            remain -= node.val

            if not node.left and not node.right:
                return remain == 0
            
            return DFS(node.left, remain) or DFS(node.right, remain)
        
        return DFS(root, targetSum)