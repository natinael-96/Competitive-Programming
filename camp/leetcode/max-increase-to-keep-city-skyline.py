class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        maxRow= [max(col) for col in grid]
        maxCol = [0]*len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxCol[j] = max(maxCol[j], grid[i][j])
        print(maxCol)
        maxS = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                maxS += min(abs(grid[j][i] - maxRow[j]), abs(grid[j][i] - maxCol[i]))
        return maxS
