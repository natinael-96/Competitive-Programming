# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = days[-1] + 1
        dp = [0]*(n)

        for i in range(1, n):
            if i in days:
                dp[i] = min(dp[i - 1] + costs[0], 
                dp[max(i - 7, 0)] + costs[1], 
                dp[max(i - 30, 0)] + costs[2])
                #print("here")
            else:
                dp[i] = dp[i - 1]
            
        #print(dp)
        return dp[-1] 
        
