# Problem: Minimum Number of Operations to Make Array XOR Equal to K - https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        xor = 0
        for i in nums:
            xor ^= i
        
        ans = 0
        while k or xor:
            if (k % 2) != (xor % 2):
                ans += 1
            
            k >>=1
            xor >>=1
        return ans
        