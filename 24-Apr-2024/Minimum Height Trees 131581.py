# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        deg = [0]*n

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
            deg[a] += 1
            deg[b] += 1

        q = deque()
        for i in range(n):
            if deg[i] == 1:
                q.append(i)

        ans = [0]

        while q:
            ans = []

            for i in range(len(q)):
                node = q.popleft()
                ans.append(node)
                for nei in adj[node]:
                    deg[nei] -= 1
                    if deg[nei] == 1:
                        q.append(nei)


        return ans
