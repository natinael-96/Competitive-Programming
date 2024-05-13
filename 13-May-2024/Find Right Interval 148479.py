# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        if n == 1:
            return [-1] if intervals[0][0] != intervals[0][1] else [0]

        ans = [-1] * n

        starts = {}
        for idx, (start, _) in enumerate(intervals):
            starts[start] = idx

        srtInter = sorted(intervals, key=lambda x: x[0])

        for i in range(n):
            curEnd = intervals[i][1]
            l, r = 0, n - 1

            while l <= r:
                mid = (l + r) // 2
                start, end = srtInter[mid]

                if start >= curEnd:
                    ans[i] = starts[start]
                    r = mid - 1
                else:
                    l = mid + 1

        return ans
