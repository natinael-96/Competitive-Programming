# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        if not mat or not mat[0]:
            return []

        rw, col = len(mat), len(mat[0])
        dxns = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque()
        visited = set()

        def inbound(x, y):
            return 0 <= x < rw and 0 <= y < col

        for i in range(rw):
            for j in range(col):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited.add((i, j))
                else:
                    mat[i][j] = -1
        
        while q:
            r, c = q.popleft()

            for dr, dc in dxns:
                nr, nc = r + dr, c + dc

                if inbound(nr, nc) and (nr, nc) not in visited:
                    q.append((nr, nc))
                    visited.add((nr, nc))
                    mat[nr][nc] = mat[r][c] + 1
        
        return mat
                    