# Problem: Find Building Where Alice and Bob Can Meet - https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)
        remain = [[] for _ in range(len(heights))]
        
        for i in range(len(queries)):
            q1, q2 = queries[i]
            left = q1 if q1 < q2 else q2
            right = q2 if q1 < q2 else q1
            
            if left == right:
                ans[i] = right
                continue
            
            hl = heights[left]
            hr = heights[right]
            
            if hl < hr:
                ans[i] = right
                continue
            
            remain[right].append((max(hl, hr), i))
        
        heap = []
        
        for j in range(len(heights)):
            while heap and heap[0][0] < heights[j]:
                _, idx = heappop(heap)
                ans[idx] = j
            
            for r in remain[j]:
                heappush(heap, r)
        
        return ans
