# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same_tree(p, q):

            if p is None and q is None:
                return True
            
            elif p is None or q is None:
                return False
            
            elif p.val != q.val:
                return False
            
            return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
        
        def DFS(node):

            if not node:
                return False
            
            if is_same_tree(node, subRoot):
                return True
            
            return DFS(node.left) or DFS(node.right)
        

        return DFS(root)