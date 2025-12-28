from typing import List
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ROW = len(grid)
        COL = len(grid[0])

        r = 0
        c = COL - 1
        count = 0
        while r < ROW and c >= 0:
                if grid[r][c] < 0:
                    count += ROW-1
                    c -= 1
                else:
                     r += 1
        return count