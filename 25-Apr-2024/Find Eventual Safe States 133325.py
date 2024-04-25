# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        deg = [0]*len(graph)
        
        for i in range(len(graph)):
            for j in graph[i]:
                adj[j].append(i)
                deg[i] += 1

        q = deque([i for i in range(len(graph)) if deg[i] == 0])

        ans = []

        while q:
            node = q.popleft()
            ans.append(node)

            for nei in adj[node]:
                deg[nei] -= 1

                if deg[nei] == 0:
                    q.append(nei)

        return sorted(ans)