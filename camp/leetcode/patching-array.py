class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        
        x = 1
        count = 0
        i = 0

        while x <= n:
            if i < len(nums) and nums[i] <= x:
                x += nums[i]
                i += 1
            else:
                x = x*2
                count += 1
        return count