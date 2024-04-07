# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        dxns = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        r, c = click[0], click[1]
        if board[r][c] == 'M':
            board[r][c] = 'X'
            return board
        
        def inbound(r, c):
            return 0 <= r < len(board) and 0 <= c < len(board[0])
        
        stack = [click]
        while stack:
            r, c = stack.pop()

            mines = 0
            for dr, dc in dxns:
                nr, nc = r + dr, c + dc

                if inbound(nr, nc) and board[nr][nc] == 'M':
                    mines += 1
            
            if mines > 0:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'

                for dr, dc in dxns:
                    nr, nc = r + dr, c + dc

                    if inbound(nr, nc) and board[nr][nc] == 'E':
                        stack.append((nr, nc))

        return board