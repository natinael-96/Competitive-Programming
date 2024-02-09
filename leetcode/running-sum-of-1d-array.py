class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runnSum = [0]*(len(nums))
        runnSum[0] = nums[0]

        for i in range(1,len(nums)):
            runnSum[i] = nums[i] + runnSum[i -1]
        
        return runnSum