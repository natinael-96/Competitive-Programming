# Problem: Pacific Atlantic Water Flow - https://leetcode.com/problems/pacific-atlantic-water-flow

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rw, col = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visit, prevHeight):
            if (r < 0 or c < 0 or r == rw or c == col or
                    (r, c) in visit or heights[r][c] < prevHeight):
                return

            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])

        for c in range(col):
            dfs(0, c, pac, heights[0][c])
            dfs(rw - 1, c, atl, heights[rw - 1][c])

        for r in range(rw):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, col - 1, atl, heights[r][col - 1])

        res = []
        for r in range(rw):
            for c in range(col):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res