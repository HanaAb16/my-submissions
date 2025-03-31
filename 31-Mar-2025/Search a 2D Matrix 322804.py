# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_row , high_row = 0 , len(matrix) - 1
        while low_row <= high_row:
            mid_row = (low_row + high_row) // 2
            low_col , high_col = 0 , len(matrix[0]) - 1
            while low_col <= high_col:
                mid_col = (low_col + high_col) // 2
                if matrix[mid_row][mid_col] < target:
                    low_col = mid_col + 1
                elif matrix[mid_row][mid_col] > target:
                    high_col = mid_col - 1
                else:
                    return True
            if high_col < 0:
                high_row = mid_row - 1
            else:
                low_row = mid_row + 1
        return False