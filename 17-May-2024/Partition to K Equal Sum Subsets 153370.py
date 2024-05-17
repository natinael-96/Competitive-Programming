# Problem: Partition to K Equal Sum Subsets - https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        if sum(nums) % k :
            return False
        
        eql = sum(nums) // k
        memo = defaultdict(int)

        def dp(i):
            if i == len(nums):
                return True
            
            for j in range(k):
                if memo[j] + nums[i]  <= eql:
                    memo[j] += nums[i]
                    if dp(i + 1):
                        return True
                    memo[j] -= nums[i]
                    if memo[j] == 0:
                        break
            return False
        return dp(0)