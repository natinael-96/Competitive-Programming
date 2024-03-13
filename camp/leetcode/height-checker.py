class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        hSort = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if hSort[i] != heights[i]:
                cnt += 1
        return cnt
