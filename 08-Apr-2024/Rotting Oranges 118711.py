# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dxns = [(1, 0),(0, 1),(0, -1),(-1, 0)]

        q = deque()
        fresh = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        if not q:
            return -1
        
        def inbound(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        time = -1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in dxns:
                    nr, nc = r + dr, c + dc

                    if inbound(nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        q.append((nr, nc))

            time += 1
        
        if fresh  == 0:
            return time
        else:
            return -1

                    
