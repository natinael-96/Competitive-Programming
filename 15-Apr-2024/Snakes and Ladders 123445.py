# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def nmCell(num):
            rw = n - 1 - (num - 1) // n

            if (n - rw) % 2:
                col = (num - 1) % n
            else:
                col = n - 1 - (num - 1) % n
            #print(rw, col)
            return rw, col

        
        visited = set()
        que = deque([(1, 0)])

        while que:
            cur, lvl = que.popleft()
            
            if cur == n**2:
                return lvl
            
            for nxt in range(cur + 1, min(cur + 6, n ** 2) + 1):
                rw, col = nmCell(nxt)

                if board[rw][col] != -1:
                    nxt  = board[rw][col]
                
                if nxt not in visited:
                    visited.add(nxt)
                    que.append((nxt, lvl + 1))
        
        return -1
