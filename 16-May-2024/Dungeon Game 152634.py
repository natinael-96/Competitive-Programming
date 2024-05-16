# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m or j == n:
                    dp[i][j] = float('inf')
                elif i == m - 1 and j == n - 1:
                    dp[i][j] = max(1, 1 - dungeon[i][j])
                else:
                    dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
                    
        return dp[0][0]