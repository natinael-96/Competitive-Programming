# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
               
        proj = [[capital[i],profits[i]] for i in range(len(profits))]
        proj.sort(key=lambda x: x[0])

        """if w >= max(capital):
            return w + sum(sorted(profits, reverse = True)[:k])"""

        heap = []
        ans = w
        for i in range(k):
            while proj and proj[0][0] <= ans:
                heappush(heap, -proj.pop(0)[1])
            
            if not heap:
                break
            ans += -heappop(heap)
        return ans