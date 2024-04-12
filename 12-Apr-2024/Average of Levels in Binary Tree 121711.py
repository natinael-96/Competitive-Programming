# Problem: Average of Levels in Binary Tree - https://leetcode.com/problems/average-of-levels-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        level = defaultdict(list)

        def dfs(rt, lvl):
            if rt is None:
                return 
            
            level[lvl].append(rt.val)
            dfs(rt.left, lvl + 1)
            dfs(rt.right, lvl + 1)
        
        dfs(root, 0)

        ans = [0]*len(level)

        for i in level.keys():
            ans[i] = sum(level[i]) / len(level[i])
        
        return ans