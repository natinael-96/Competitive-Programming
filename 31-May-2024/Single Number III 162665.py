# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        val = nm1 = nm2 = 0
        for i in nums:
            val ^= i

        val &= -val
        for i in nums:
            if i & val: 
                nm2 ^= i
            else: 
                nm1 ^= i

        return [nm1, nm2]