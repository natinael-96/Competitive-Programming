# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        n = len(s)
        if s == '':
            return ['']
        ans = []

        def helper(i, path):
            if len(path) == n:
                ans.append(path[:])
                return
            if s[i].isalpha():
                helper(i + 1, path + s[i].swapcase())
            helper(i + 1, path + s[i])
        
        helper(0, '')
        return ans