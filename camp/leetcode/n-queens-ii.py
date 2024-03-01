class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def safe(grid, row,col):
            
            # left

            for i in range(col):
                if grid[row][i] == 'Q':
                    return False
            
            # lower diagonal

            for i,j in zip(range(row,n,1),range(col,-1,-1)):
                if grid[i][j] == 'Q':
                    return False
            
            # upper diagonal

            for i, j in zip(range(row,-1,-1), range(col,-1,-1)):
                if grid[i][j] == 'Q':
                    return False
            return True
        ans = [0]
        def helper(grid,col):
            if col >= n:
                ans[0] += 1
                return
                
            for i in range(n):

                if safe(grid,i,col):
                    grid[i][col] = 'Q'
                    helper(grid,col+1)
                    grid[i][col] = '.'

        grid = [['.' for _ in range(n)] for _ in range(n)]
        helper(grid, 0)
        return ans[0]