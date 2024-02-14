class Solution:
    def maxScore(self, s: str) -> int:
        lftSm = 0
        rgSm = sum([int(x) for x in s])
        maxSp = 0
        for i in range(len(s)-1):
            lftSm += int(s[i])
            rgSm -= int(s[i])
            maxSp = max(maxSp,i+ 1 - lftSm + rgSm)
        return maxSp
