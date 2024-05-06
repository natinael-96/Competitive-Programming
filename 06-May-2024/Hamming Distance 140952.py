# Problem: Hamming Distance - https://leetcode.com/problems/hamming-distance/

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        
        xor = x ^ y

        ans = 0
        while xor:
            ans += xor&1
            xor >>= 1
                    
        return ans