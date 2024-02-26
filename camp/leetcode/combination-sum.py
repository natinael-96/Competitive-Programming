class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def helper(i,path):
            if sum(path) >= target :
                if sum(path) == target:
                    ans.append(path[:])
                return
            
            for j in range(i,len(candidates)):
                if candidates[j] <=target:
                    path.append(candidates[j])
                    helper(j,path)
                    path.pop()
        helper(0,[])
        return ans