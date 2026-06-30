# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_order_idxs = {val: idx for idx, val in enumerate(inorder)}

        # root = TreeNode(val = preorder[0])

        # root.left = self.buildTree(
        #     preorder[1:in_order_idxs[preorder[0]]+1],
        #     inorder[:in_order_idxs[preorder[0]]]
        # )
        # root.right = self.buildTree(
        #     preorder[in_order_idxs[preorder[0]]+1:],
        #     inorder[in_order_idxs[preorder[0]]+1:]
        # )
        # return root
        self.preorder_idx = 0
        def build_tree(left, right):
            if left>right:
                return None

            root = TreeNode(val=preorder[self.preorder_idx])
            mid = in_order_idxs[preorder[self.preorder_idx]]
            self.preorder_idx+=1

            root.left = build_tree(left, mid-1)
            root.right = build_tree(mid+1,right)

            return root
        return build_tree(0, len(preorder)-1)
        
            
