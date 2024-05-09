# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: list[int]) -> int:

        if len(nums) < 2:
            return max(nums)

        dp = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            dp = dp[-1], max(dp[-1], dp[-2] + nums[i])
        
        return dp[-1]