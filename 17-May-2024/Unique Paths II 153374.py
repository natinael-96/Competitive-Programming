# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:     
        m, n = len(obstacleGrid), len(obstacleGrid[0]) 
        dp = [[0]*(n) for _ in range(m)]
        
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 1:
                    if i > 0:  
                        dp[i][j] += dp[i - 1][j]
                    if j > 0:  
                        dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]
