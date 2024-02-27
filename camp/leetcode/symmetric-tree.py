# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def helper(lftrt, rghtrt):
            if not lftrt and not rghtrt:
                return True
            if not lftrt or not rghtrt:
                return False
            return lftrt.val == rghtrt.val and helper(lftrt.left, rghtrt.right) and helper(lftrt.right, rghtrt.left)
        return helper(root.left, root.right)
