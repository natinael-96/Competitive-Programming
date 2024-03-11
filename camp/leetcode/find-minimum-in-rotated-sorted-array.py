class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1

        while l <= r:
            mid = (l + r) // 2

            if  nums[(mid + 1) % n] >= nums[mid] <= nums[(mid - 1 + n) % n]:
                return nums[mid]

            elif nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return nums[0]
