# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        memo = {}

        def helper(s):
            n = len(s)
            if not s:
                return [[]]
            if s in memo:
                return memo[s]
            
            cur = []
            for i in range(1, n + 1):
                pre = s[:i]
                if pre == pre[::-1]:
                    for j in helper(s[i:]):
                        cur.append([pre] + j)
            memo[s] = cur
            return memo[s]
        
        return helper(s)