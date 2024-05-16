# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        memo = {}
        def dp(i, j):
            if i > j:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            strt, end = piles[i] + dp(i + 1, j), piles[j] + dp(i, j - 1)
            memo[(i, j)] = max(strt, end)
            return memo[(i, j)]
        
        return dp(0, len(piles) - 1)