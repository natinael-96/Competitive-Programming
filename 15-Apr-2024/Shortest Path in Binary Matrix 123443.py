# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dxns = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1)]
        n = len(grid)

        if grid[0][0] != 0:
            return -1
        
        q = deque()
        q.append((0, 0, 1))
        step = float('inf')

        grid[0][0] = 1
        def inbound(x, y):
            return 0 <= x < n and 0 <= y < n

        while q:
            x, y, st = q.popleft()

            if (x, y) == (n -1, n -1):
                step = min(st, step)

            for dx, dy in dxns:
                nx, ny = x + dx, y + dy

                if inbound(nx, ny) and grid[nx][ny] == 0:
                    q.append((nx, ny, st + 1))
                    grid[nx][ny] = 1

        return step if step != float('inf') else -1



