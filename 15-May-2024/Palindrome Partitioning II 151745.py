# Problem: Palindrome Partitioning II - https://leetcode.com/problems/palindrome-partitioning-ii/

class Solution:
    def minCut(self, s: str) -> int:
        memo = {}
        def helper(s):
            n = len(s)
            if not s:
                return 0
            if s in memo:
                return memo[s]
            
            mnct = float('inf')
            for i in range(1, n + 1):
                pre = s[:i]
                if pre == pre[::-1]:
                    j = helper(s[i:])
                    mnct = min(mnct, 1 + j)
            memo[s] = mnct
            return mnct

        return helper(s) - 1
