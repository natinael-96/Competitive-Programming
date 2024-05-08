# Problem: Maximum Performance of a Team - https://leetcode.com/problems/maximum-performance-of-a-team/

class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        
        engs = [(speed[i], efficiency[i]) for i in range(n)]
        engs.sort(key = lambda x : x[1], reverse = True)

        ans = 0
        speed = 0

        heap = []
        for s, e in engs:
            if len(heap) == k:
                speed -= heappop(heap)

            speed += s
            heappush(heap, s)
            ans = max(ans, e * speed)
        
        return ans % (10 ** 9 + 7)