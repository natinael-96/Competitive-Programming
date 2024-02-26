# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def travers(root, minV = float('-inf'), maxV = float('inf')):
            if root is None:
                return True
            if not (minV < root.val < maxV):
                return False
            left = travers(root.left, minV, root.val) 
            right = travers(root.right, root.val, maxV)
            
            return left and right
        return travers(root)
