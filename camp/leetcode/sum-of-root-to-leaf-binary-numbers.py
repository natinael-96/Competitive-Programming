# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        out = []

        def helper(rt, path):
            if rt is None:
                return 
            
            if rt.left is None and rt.right is None:
                path.append(str(rt.val))
                num = int("".join( path),2)
                out.append(num)
                path.pop()
                return
            
            path.append(str(rt.val))
            helper(rt.left, path)
            helper(rt.right, path)
            path.pop()
        helper(root, [])
        return sum(out)
