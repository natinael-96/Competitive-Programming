# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        if root == q or root == p or not root:
            return root
        
        root_left = self.lowestCommonAncestor(root.left, p, q)
        root_right = self.lowestCommonAncestor(root.right, p, q)

        if root_left and root_right:
            return root
        return root_left or root_right
                

        

