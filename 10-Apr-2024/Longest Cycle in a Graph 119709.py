# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        visited = set()
        ans = [-1]

        def dfs(node):
            if node == -1:
                return None, 0
            if node in visited:
                return node, 1
            
            visited.add(node)
            
            cNode, l = dfs(edges[node])
            if node == cNode:
                ans[0] = max(ans[0], l)
            
            return cNode, l + 1
        
        for i in range(len(edges)):
            if edges[i] != -1:
                dfs(i)
        
        return ans[0]
