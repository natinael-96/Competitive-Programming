# Problem: All Nodes Distance K in Binary Tree - https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        adj = defaultdict(list)

        def trav(rt):
            if root is None:
                return

            if rt.left:
                adj[rt.left.val].append(rt.val)
                adj[rt.val].append(rt.left.val)
                trav(rt.left)

            if rt.right:
                adj[rt.right.val].append(rt.val)
                adj[rt.val].append(rt.right.val)
                trav(rt.right)

        trav(root)
        #print(adj)
        
        ans = []
        vis = set()

        def dfs(node, lvl):
            if node in vis:
                return
            
            vis.add(node)
            if lvl == k:
                ans.append(node)
                return

            for nei in adj[node]:
                dfs(nei, lvl + 1)

        
        dfs(target.val, 0)
        
        return ans
            
            
            