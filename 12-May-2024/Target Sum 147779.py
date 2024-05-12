# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        sm = sum(nums)
        if (target + sm) % 2 != 0 :
            return 0
        targ = (sm + abs(target))//2
        dp = [0]*(targ + 1)
        dp[0] = 1

        for nm in nums:
            for i in range(targ, nm - 1, -1):
                dp[i] += (dp[i - nm]) 
        return dp[-1]

        
