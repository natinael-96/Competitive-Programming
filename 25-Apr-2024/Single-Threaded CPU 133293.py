# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted((ent, prot, i) for i , (ent, prot) in enumerate(tasks))

        ans = []
        heap = []
        time = 0
        for ent, prot, i in tasks:
            while heap and ent > time:
                pt, idx = heapq.heappop(heap)

                ans.append(idx)
                time += pt

            time = max(time, ent)
            heapq.heappush(heap, (prot, i))
        while heap:
            pro, i = heappop(heap)
            ans.append(i)
        return ans