class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def canBe(m):
            currSm, d = 0, 1

            for w in weights:
                if currSm + w <= m:
                    currSm += w
                else:
                    d += 1
                    currSm = w
            return d <= days

        l, r = max(weights), sum(weights)

        while l <= r:

            mid = (l + r)//2

            if canBe(mid):
                r = mid-1
            else:
                l = mid + 1
        return l
