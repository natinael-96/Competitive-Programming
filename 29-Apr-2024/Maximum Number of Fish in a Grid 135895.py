# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rank = {}
        par = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rank[(i,j)] = 1
                par[(i,j)] = (i,j)
        def union(i,j):
            if par[i] == par[j]:
                return 
            else:
                p1 = find(i)
                p2 = find(j)
                if rank[p1] > rank[p2] :
                    rank[p1] += rank[p2]
                    par[p2] = p1
                else :
                    rank[p2] += rank[p1]
                    par[p1] = p2
        def find(i):
            if par[i] == i:
                return i
            else:
                return find(par[i])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    continue
                else:
                    if grid[i][max(j-1,0)] > 0:

                        union((i,j),(i,max(j-1,0)))
                    
                    if grid[i][min(j+1,len(grid[0])-1)] > 0:
                        
                        union((i,j),(i,min(j+1,len(grid[0]) - 1)))
                    
                    if grid[max(i-1,0)][j] > 0:
                        
                        union((i,j),(max(i-1,0),j))
                    
                    if grid[min(i+1,len(grid)-1)][j] > 0:
                        
                        union((i,j),(min(i+1,len(grid)-1),j))
        res = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    p1 = find((i,j))
                    if p1 in res:
                        res[p1] += grid[i][j]
                    else :
                        res[p1] = grid[i][j]
        if len(res.values()) == 0:
            return 0
        return max(res.values())