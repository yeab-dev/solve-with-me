from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(k: int):
            hours = 0
            for pile in piles:
                if hours > h:
                    return False
                hours += math.ceil(pile / k)
            return hours <= h 
        left, right = 1, len(piles)
        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                right = mid - 1

            else:
                left = mid + 1
        return left