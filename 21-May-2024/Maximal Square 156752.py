# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0]*(m + 1) for _ in range(n + 1)] 

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                #print(i, j)
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    #print('h')
        mx = 0
        for i in dp:
            mx = max(mx, max(i))
        #print(dp)
        return mx * mx




                    

