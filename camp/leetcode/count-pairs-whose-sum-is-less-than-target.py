class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        # 0 indx, nums, len - n and target  
        # return pair i , j  (i < j) where nums[i] + nums[j] < target
        nums.sort()
        l , r = 0, len(nums) - 1
        count = 0
        while l < r:
            if nums[l] + nums[r] < target:
                count += r - l
                l += 1
            else:
                r -= 1
        return count 