# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        q = deque()

        while root:
            if root.left:
                if root.left.val != root.val:
                    return False
                q.append(root.left)
            if root.right:
                if root.right.val != root.val:
                    return False
                q.append(root.right)
            if q:
                root = q.popleft()
            else:
                break
        return True