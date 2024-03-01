class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        diagonals = defaultdict(list)
        rows, columns = len(matrix), len(matrix[0])
        res = []
        
        for r in range(rows):
            for c in range(columns):
                diagonals[(r + c)].append(matrix[r][c])

        for j in range(len(diagonals.keys())):
            if j % 2 == 1:
                res.extend(diagonals[j])
            else:
                # reverse
                res.extend(diagonals[j][::-1])

        return res
