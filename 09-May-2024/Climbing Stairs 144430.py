# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [1, 2]

        if n < 2:
            return dp[n - 1]
        
        for i in range(2, n):
            dp = dp[-1], dp[-1] + dp[-2]
        
        return dp[-1]