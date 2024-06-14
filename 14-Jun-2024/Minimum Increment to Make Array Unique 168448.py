# Problem: Minimum Increment to Make Array Unique - https://leetcode.com/problems/minimum-increment-to-make-array-unique/

class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        flag = 0
        ans = 0

        for i in nums:
            flag = max(flag, i)
            ans += flag - i
            flag += 1
        return ans