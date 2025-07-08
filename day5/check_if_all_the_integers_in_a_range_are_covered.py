from typing import List
class Solution:
    def isCovered(self, ranges:List[List[int]], left: int, right:int) -> bool:
        ranges.sort(key=lambda x: x[0])
        for range in ranges:
            while left >= range[0] and left <= range[1]:
                left += 1
        return left > right