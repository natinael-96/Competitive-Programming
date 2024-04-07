# Problem: Binary Tree Level Order Traversal - https://leetcode.com/problems/binary-tree-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = defaultdict(list)
        ans[0].append(root.val)
        q = deque([root])
        level = 0

        while q:
            level += 1
            for _ in range(len(q)):
                root = q.popleft()
                if root.left:
                    q.append(root.left)
                    ans[level].append(root.left.val)
                if root.right:
                    q.append(root.right)
                    ans[level].append(root.right.val)
                
        
        return [i for i in ans.values()]
            
            
