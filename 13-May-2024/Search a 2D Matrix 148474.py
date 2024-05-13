# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n * m - 1

        while l <= r:
            mid = (l + r) // 2
            rw = mid // m
            col = mid % m

            if matrix[rw][col] == target:
                return True
            elif matrix[rw][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False