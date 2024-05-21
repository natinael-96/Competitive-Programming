# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        
        if stones[1] - stones[0] != 1:
            return False
        
        if len(stones) == 2 and stones[0] == 0 and stones[1] == 1:
            return True
        
        dp = {}
        for i in stones:
            dp[i] = set()
        dp[0].add(0)

        for i in stones:
            #print(i)
            for k in dp[i]:
                if k > 1 and (i + k - 1) in dp:
                    dp[i + k - 1].add(k - 1)
                if (i + k) in dp:
                    dp[i + k].add(k)
                if (i + k + 1) in dp:
                    dp[i + k + 1].add(k + 1)
        
        return len(dp[stones[-1]]) > 0


            