# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}

        def helper(i, byn):
            if (i, byn) in memo:
                return memo[(i, byn)]
            
            if i >= len(prices):
                return 0
            
            cooldwn = helper(i + 1, byn)

            if byn:
                cur = helper(i + 1, not byn) - prices[i]
                memo[(i, byn)] = max(cur, cooldwn)
            else:
                cur = helper(i + 2, not byn) + prices[i]
                memo[(i, byn)] = max(cur, cooldwn)
            
            return memo[(i, byn)]
        return helper(0, True)