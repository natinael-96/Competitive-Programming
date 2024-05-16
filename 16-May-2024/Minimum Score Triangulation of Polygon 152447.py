# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        
        memo = {}
        def dp(i, j):
            if j == i + 1:
                return 0
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            cur = float('inf')
            for k in range(i + 1, j):
                crScr = values[i] * values[j] * values[k]
                side = dp(i, k) + dp(k, j)
                cur = min(cur, crScr + side)
            memo[(i, j)] = cur
            return memo[(i, j)]
        
        return dp(0, len(values) - 1)