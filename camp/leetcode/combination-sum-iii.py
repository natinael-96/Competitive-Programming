from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        out = []

        def backTrack(ind, path):
            if len(path) == k and sum(path) == n:
                out.append(path[:])
                return

            for i in range(ind, 10):
                if i <= n:
                    path.append(i)
                    backTrack(i + 1, path)
                    path.pop()

        backTrack(1, [])
        return out
