# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        ans = []

        def travers(rt):
            if rt is None:
                return 
            
            travers(rt.left)
            ans.append(rt.val)
            travers(rt.right)
        travers(root)
        return ans[k-1]