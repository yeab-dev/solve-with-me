import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))

        while j >= i:
            square_sum = i ** 2 + j ** 2
            if square_sum > c:
                j -= 1
            elif square_sum < c:
                i += 1
            else:
                return True
        return False