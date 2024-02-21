class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        costs.sort(key = lambda x: x[1] - x[0])
        aTot = 0
        
        
        for i in range(n):
            if i < n//2:
                aTot += costs[i][1]
            else:
                aTot += costs[i][0]
        return aTot 
