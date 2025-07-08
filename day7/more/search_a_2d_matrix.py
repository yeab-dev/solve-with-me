from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int)-> bool:
        COL = len(matrix[0])-1

        for row in matrix:
            if row[0] <= target <= row[COL]:
                return target in row
        return False
