# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        
        

        def smNum(root, arrS):
            if root is None:
                return 0
            arrS = arrS * 10 + root.val

            if root.left is None and root.right is None:
                return arrS
            return smNum(root.left, arrS) + smNum(root.right, arrS)
            
        return smNum(root, 0)