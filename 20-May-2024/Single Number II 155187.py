# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ons, tws = 0, 0

        for i in nums:
            tws |= ons & i
            ons ^= i

            temp = ons & tws
            ons &= ~temp
            tws &= ~temp
        return ons
