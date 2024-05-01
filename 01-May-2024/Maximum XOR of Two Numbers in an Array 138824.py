# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        mask = 0
        maxm = 0
        for i in range(32, -1, -1):
            mask = mask | 1 << i

            pref = {mask & nm for nm in nums}

            possbl = maxm | 1 << i
            for pre in pref:
                if (possbl ^ pre) in pref:
                    maxm = possbl
                    break
        return maxm 