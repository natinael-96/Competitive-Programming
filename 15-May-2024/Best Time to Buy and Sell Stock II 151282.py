# Problem: Best Time to Buy and Sell Stock II - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}
        n = len(prices)

        def helper(dy, hold):
            if dy == n:
                return 0
            
            if (dy, hold) in dp:
                return dp[(dy, hold)]
            
            nottake = helper(dy + 1, hold)
            if not hold:
                take = helper(dy + 1, True) - prices[dy]
            else:
                take = helper(dy + 1, False) + prices[dy]

            dp[(dy, hold)] = max(take, nottake)
            return dp[(dy, hold)]
        
        return helper(0, False)