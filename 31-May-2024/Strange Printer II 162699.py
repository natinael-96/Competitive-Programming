# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        
        rw, col = len(targetGrid), len(targetGrid[0])
        colors = set()
        for i in range(rw):
            for j in range(col):
                colors.add(targetGrid[i][j])
        

        bound = {c : [float('inf'), float('inf'), float('-inf'), float('-inf')] for c in colors}

        for i in range(rw):
            for j in range(col):
                c = targetGrid[i][j]
                bound[c][0] = min(bound[c][0], i)
                bound[c][1] = min(bound[c][1], j)
                bound[c][2] = max(bound[c][2], i)
                bound[c][3] = max(bound[c][3], j)
        
        graph = defaultdict(set)

        for c, (up, lft, dwn, rgt) in bound.items():
            visited = set()
            for i in range(up, dwn + 1):
                for j in range(lft, rgt + 1):
                    if targetGrid[i][j] != c and targetGrid[i][j] not in visited:
                        graph[c].add(targetGrid[i][j])
                        visited.add(targetGrid[i][j])
        
        visited = {c : 0 for c in colors}
        def dfs(c):
            if visited[c] == 1:
                return False
            if visited[c] == 2:
                return True
            visited[c] = 1
            for nei in graph[c]:
                if not dfs(nei):
                    return False
            visited[c] = 2
            return True
        
        for c in colors:
            if visited[c] == 0 and not dfs(c):
                return False
        return True

        

  

