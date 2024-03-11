from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target
        ans = [-1, -1]

        if target not in nums:
            return ans

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        ans[0] = l


        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] <= target: 
                l = mid + 1
            else:
                r = mid - 1

        ans[1] = r

        return ans
