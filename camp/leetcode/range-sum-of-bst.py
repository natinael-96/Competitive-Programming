# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        out = []
        def rangSum(root, low,high):
            if root is None:
                return
            if low <= root.val <= high:
                out.append(root.val)
            rangSum(root.left, low,high)
            rangSum(root.right, low,high)
        rangSum(root,low,high)
        return sum(out)
            
            