# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans = 0

        for i in nums:
            ans ^= i
        
        for i in range(len(nums) + 1):
            ans ^= i
        
        return ans
