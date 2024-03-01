from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        out = [False]

        def search(i, j, k, visited):
            if k == len(word):
                out[0] = True
            if (
                i < 0
                or j < 0
                or i >= len(board)
                or j >= len(board[0])
                or k >= len(word)  
                or word[k] != board[i][j]
                or visited[i][j]
            ):
                return
            visited[i][j] = True
            search(i - 1, j, k + 1, visited)
            search(i + 1, j, k + 1, visited)
            search(i, j - 1, k + 1, visited)
            search(i, j + 1, k + 1, visited)
            visited[i][j] = False

        def exist(board, wrd):
            if not board or not board[0] or not wrd:
                return False

            n = len(board[0])
            m = len(board)

            for i in range(m):
                for j in range(n):
                    if board[i][j] == wrd[0]:
                        search(i, j, 0, [[False] * n for _ in range(m)])

        exist(board, word)
        return out[0]


