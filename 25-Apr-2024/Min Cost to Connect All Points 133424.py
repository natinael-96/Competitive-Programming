# Problem: Min Cost to Connect All Points - https://leetcode.com/problems/min-cost-to-connect-all-points/

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        n = len(points)

        tot = 0
        dist = [float('inf')]*n

        strt = 0
        dist[strt] = 0
        visited = set()
        heap = [(0, strt)]

        while heap:
            dis, cur = heappop(heap)

            if cur not in visited:

                visited.add(cur)
                tot += dis

                for i in range(n):
                    if i not in visited:

                        val = abs(points[cur][0] - points[i][0])
                        val += abs(points[cur][1] - points[i][1])

                        if val < dist[i]:
                            dist[i] = val
                            heappush(heap, (val, i))

        return tot