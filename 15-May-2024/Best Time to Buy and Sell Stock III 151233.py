# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo = {}
        n = len(prices)

        def dp(dy, hold, tran):
            if dy == n or tran == 0:
                return 0
            
            if (dy, hold, tran) in memo:
                return memo[(dy, hold, tran)]
            
            nottake = dp(dy + 1, hold, tran)

            if not hold:
                take = dp(dy + 1, True, tran) - prices[dy]
            else:
                take = dp(dy + 1, False, tran - 1) + prices[dy]
            
            memo[(dy, hold, tran)] = max(nottake, take)
            return memo[(dy, hold, tran)]
        
        return dp(0, False, 2)
