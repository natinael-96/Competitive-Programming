class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        soln = []
        
        def backTrack(nxt, ans):
            if len(ans) == k:
                soln.append(ans[:])
                return 
            
            for i in range(nxt, n+1):
                ans.append(i)
                backTrack(i+1,ans)
                ans.pop()
        backTrack(1, [])
        return soln
