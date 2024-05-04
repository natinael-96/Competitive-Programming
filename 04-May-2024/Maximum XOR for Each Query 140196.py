# Problem: Maximum XOR for Each Query - https://leetcode.com/problems/maximum-xor-for-each-query/

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        
        mx = (1 << maximumBit) - 1
        ans = []
        xor = 0
        for i in nums:
            xor = (xor ^ i) & mx
            k = xor ^ mx
            ans.append(k)
        
        ans = ans[::-1]
        return ans
        