# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        # get height
        def helper(root, is_left = True):
            node = root
            height = 0

            while node:
                height += 1
                node = node.left if is_left else node.right
            
            return height

        if root is None:
            return 0

        left_height = helper(root)
        right_height = helper(root, False)

        if left_height == right_height:
            return 2 ** left_height - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)