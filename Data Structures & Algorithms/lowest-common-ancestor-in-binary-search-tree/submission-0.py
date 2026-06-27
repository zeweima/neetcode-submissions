# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        

        def dfs(node):
            if node is None:
                return None
            if node.val == p.val:
                return node
            if node.val == q.val:
                return node
            
            left_ = dfs(node.left)
            right_ = dfs(node.right)

            if left_ and right_:
                return node
            
            if left_:
                return left_
            if right_:
                return right_
            # return None
        
        return dfs(root)