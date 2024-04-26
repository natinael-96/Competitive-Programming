# Problem: All Ancestors of A Node in Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        graph = defaultdict(list)
        deg = defaultdict(int)

        for a, b in edges:
            graph[a].append(b)
            deg[b] += 1
        
        q = deque([i for i in range(n) if deg[i] == 0])
        ans = [set() for _ in range(n)]

        while q:
            node = q.popleft()

            for nei in graph[node]:
                ans[nei].add(node)
                ans[nei].update(ans[node])
                deg[nei] -= 1
                if deg[nei] == 0:
                    q.append(nei)
        
        return [sorted(i) for i in ans]

