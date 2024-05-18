# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        n = len(questions)
        dp = [-1] * (n + 1)
        q = questions

        dp[n - 1] = q[n - 1][0]

        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], q[i][0])
            if (i + q[i][1]) < n:
                dp[i] = max(dp[i], q[i][0] + dp[i + q[i][1] + 1])

        return dp[0]
