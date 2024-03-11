class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def isSuf(m):
            return sum(ceil(i/m) for i in piles) <= h
        
        while l < r:
            mid = (l + r)//2

            if isSuf(mid):
                r = mid
            else:
                l = mid + 1
        return l