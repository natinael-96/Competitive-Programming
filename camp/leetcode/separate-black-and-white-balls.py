class Solution:
    def minimumSteps(self, s: str) -> int:
        
        cntZ  = 0
        ans = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                cntZ += 1
            else:
                ans += cntZ
        return ans