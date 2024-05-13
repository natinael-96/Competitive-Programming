# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices))
        mn = prices[0]

        for i in range(1, len(prices)):
            dp[i] = max(dp[i - 1], prices[i] - mn)
            mn = min(mn, prices[i])
        #print(dp)
        return dp[-1]
