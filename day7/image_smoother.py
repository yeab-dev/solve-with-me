from math import floor
from typing import List
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])
        result = [[0] * COLS for _ in range(ROWS)]

        for row in range(ROWS):
            for col in range(COLS):
                total, count = 0,0
                for i in range(row-1, row+2):
                    for j in range(col-1, col+2):
                        if i < 0 or i == ROWS or j < 0 or j == COLS:
                            continue
                        total += img[i][j]
                        count += 1
                result[row][col] = total // count
        return result

print(Solution().imageSmoother([[1,1,1],[1,0,1],[1,1,1]]))