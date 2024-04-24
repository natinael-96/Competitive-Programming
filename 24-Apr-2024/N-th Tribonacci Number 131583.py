# Problem: N-th Tribonacci Number - https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n < 2:
            return n
        
        dp = [0, 1, 1]

        for i in range(3, n + 1):
            nxt = dp[0] + dp[1] + dp[2]
            dp[0], dp[1], dp[2] = dp[1], dp[2], nxt

        return dp[-1]