# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        val = m * k
        if val > n:
            return -1
        
        def possible(bloomDay, day, m, k):
            cnt = 0
            num = 0
            for bd in bloomDay:
                if bd <= day:
                    cnt += 1
                else:
                    num += cnt // k
                    cnt = 0
            num += cnt // k
            return num >= m
            
        l = float('inf')
        r = float('-inf')
        for i in bloomDay:
            l = min(i, l)
            r = max(i, r)
        
        while l <= r:
            mid = l + (r - l) // 2
            if possible(bloomDay, mid, m, k):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
    
        