from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        result = [[0] * len(matrix) for _ in range(len(matrix[0]))]

        for i in range(ROWS):
            for j in range(COLS):
                result[j][i] = matrix[i][j]
        return result