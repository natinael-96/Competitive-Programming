class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def safe(grid, row, col):

            for i in range(col):
                if grid[row][i] == 'Q':
                    return False
            
            # lower diagonal
            for i,j in zip(range(row,n,1), range(col,-1,-1)):
                if grid[i][j] == 'Q':
                    return False

            # uper diagonal
            for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
                if grid[i][j] == 'Q':
                    return False

            return True
            
        ans = []
        def helper(grid, col):
            if col >= n:
                ans.append([''.join(rw[:]) for rw in grid])
                return 

            for i in range(n):
                if safe(grid, i, col):

                    grid[i][col] = 'Q'
                    helper(grid, col + 1)
                    grid[i][col] = '.'

        grid = [['.' for i in range(n)] for i in range(n)]
            
        helper(grid, 0)
        return ans
        



                