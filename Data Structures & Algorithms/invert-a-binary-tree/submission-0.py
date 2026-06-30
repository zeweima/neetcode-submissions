# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root == None:
            return None
        
        left_invert = self.invertTree(root.right)
        right_inver = self.invertTree(root.left)
        root.left = left_invert
        root.right = right_inver

        return root