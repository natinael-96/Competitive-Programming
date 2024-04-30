# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        deg = [0] * (n)

        for a, b in edges:
            deg[b] += 1
        
        return -1 if deg.count(0) > 1 else deg.index(0)