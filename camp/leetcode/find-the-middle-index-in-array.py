class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        preSum = 0
        rSum = sum(nums)

        for i in range(len(nums)):
            if preSum == rSum - nums[i]:
                return i
            preSum += nums[i]

            rSum -= nums[i]
        return -1
