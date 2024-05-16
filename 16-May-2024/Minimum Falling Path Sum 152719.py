# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        
        
        dp = matrix[-1]
        
        for i in range(n - 2, -1, -1):
            nw = [0]*n
            for j in range(n):
                nw[j] = matrix[i][j] + min(
                    dp[j], 
                    dp[j - 1] if j > 0 else float('inf'),  
                    dp[j + 1] if j < n -1 else float('inf'))
            dp = nw

        return min(dp)