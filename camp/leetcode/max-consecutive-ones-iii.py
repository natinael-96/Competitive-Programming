class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                k -= 1
            
            if k < 0:
                k += 1 - nums[l]
                l += 1
        return r - l + 1