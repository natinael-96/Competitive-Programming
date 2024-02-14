class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        preSum = nums[0]

        for i in range(1,len(nums)):
            curr = preSum + nums[i]
            preSum = max(nums[i], curr)
            maxSum = max(preSum, maxSum)
        return maxSum