# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm = sum(nums)
        if sm % 2 == 1:
            return False
        
        sm //=2
        dp = [False]*(sm + 1)

        dp[0] = True
        for i in nums:
            for j in range(sm, i-1, -1):
                #print(dp, j, j-i)
                dp[j] = (dp[j] or dp[j - i])
                #if dp[j]: print("h")
        #print(dp)
        return dp[-1]
