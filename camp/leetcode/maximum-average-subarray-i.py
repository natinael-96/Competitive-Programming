class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        wSum = sum(nums[:k])
        maxAve = wSum/k
        for i in range(k,len(nums)):
            wSum += nums[i] - nums[i - k]
            currAve = wSum/k
            maxAve = max(maxAve, currAve)
        
        return maxAve