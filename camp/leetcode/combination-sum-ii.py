class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        out = []
        candidates.sort()
        def backTrack(ind, path):
            if sum(path) >= target:
                if sum(path) == target:
                    out.append(path[:])
                return

            for i in range(ind, len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                backTrack(i+1, path)
                path.pop()
        backTrack(0, [])
        return out
            