class Solution:
    def numberOfWays(self, s: str) -> int:
        
        z = s.count('0')

        ones = len(s) - z

        zPre = 0
        onePre = 0
        ans = 0

        for i in s:
            if i == '0':
                ans += onePre * (ones - onePre)
                zPre += 1
            else:
                ans += zPre * (z - zPre)
                onePre += 1

        return ans


