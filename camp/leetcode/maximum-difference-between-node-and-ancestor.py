# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxD = [0]
        def maxxAnc(root, minV, maxV,maxD):
            if not root:
                return

            minV = min(root.val, minV)
            maxV = max(root.val, maxV)
            maxD[0] = max(maxD[0], maxV - minV)

            maxxAnc(root.left, minV, maxV, maxD)
            maxxAnc(root.right, minV, maxV, maxD)
            
        maxxAnc(root, root.val, root.val, maxD)
        return maxD[0]
        
