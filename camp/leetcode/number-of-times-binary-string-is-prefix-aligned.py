class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        tot = 0
        cnt = 0
        for i, f in enumerate(flips):
            tot += f
            if tot == (i+1)*(i+2)//2:
                cnt += 1
        return cnt