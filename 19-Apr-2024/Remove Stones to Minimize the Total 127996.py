# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles] 
        heapq.heapify(piles)

        for i in range(k):
            cur = math.ceil(-heapq.heappop(piles)/2)
            heapq.heappush(piles, -cur)
        return -sum(piles)
