class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        counter = 0
        sums = defaultdict(int)
        preSum = 0
        
        for i in range(len(nums)):
            preSum += nums[i]
            if preSum == goal:
                counter += 1
            if preSum - goal in sums:
                counter += sums[preSum - goal]
            sums[preSum] += 1
            



        return counter
 