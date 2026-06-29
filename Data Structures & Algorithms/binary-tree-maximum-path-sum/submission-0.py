# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val

        def dfs(node):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            tmp_max = node.val + max(0, left) + max(0, right)
            # print(tmp_max)
            self.max_sum = max(self.max_sum, tmp_max)

            return node.val + max(0, left, right)
        
        dfs(root)
        return self.max_sum
