# Problem: Minimum XOR Sum of Two Arrays - https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums2)
        memo = {}

        def dp(i, mask):
            if i >= n:
                return 0
            if (i, mask) in memo:
                return memo[(i, mask)]
            min_xor_sum = float('inf')
            for j in range(n):
                if mask & (1 << j):
                    new_mask = mask ^ (1 << j)
                    xor_sum = (nums1[i] ^ nums2[j]) + dp(i + 1, new_mask)
                    min_xor_sum = min(min_xor_sum, xor_sum)
            memo[(i, mask)] = min_xor_sum
            return min_xor_sum
        
        return dp(0, (1 << n) - 1)
