# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        if not board:
            return
        
        def inbound(x, y):
            return 0 <= x < len(board) and 0 <= y < len(board[0])
        
        dxns = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(x, y):
            if not inbound(x, y) or board[x][y] != 'O':
                return
            board[x][y] = 'V'  # Mark current cell as visited
            for dx, dy in dxns:
                nx, ny = x + dx, y + dy
                dfs(nx, ny)
        
        for i in range(len(board)):
            dfs(i, 0)
            dfs(i, len(board[0]) - 1)
        
        for j in range(len(board[0])):
            dfs(0, j)
            dfs(len(board) - 1, j)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'
