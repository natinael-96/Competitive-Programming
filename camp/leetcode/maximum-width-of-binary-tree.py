from collections import defaultdict
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = defaultdict(lambda: [float('inf'), float('-inf')])  
        mxDif = [0]

        def traverse(rt, index, lvl):
            if not rt:
                return 

            level[lvl][0] = min(level[lvl][0], index)
            level[lvl][1] = max(level[lvl][1], index)
            mxDif[0] = max(mxDif[0], level[lvl][1] - level[lvl][0])

            traverse(rt.left, 2*index, lvl+1)
            traverse(rt.right, 2*index+1, lvl+1)

        traverse(root, 0, 0)
        return mxDif[0] + 1
