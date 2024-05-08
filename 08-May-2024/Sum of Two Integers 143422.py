# Problem: Sum of Two Integers - https://leetcode.com/problems/sum-of-two-integers/description/

class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xffffffff
        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry

        return a if a <= 0x6FFFFFFF else ~(a ^ mask)