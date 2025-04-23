class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        count = 0

        while target > 1:
            if target % 2 == 0 and maxDoubles >= 1:
                target //= 2
                maxDoubles -= 1
                count += 1
            elif maxDoubles >= 1:
                target -= 1
                count += 1
            else: 
                count += target - 1
                return count
        return count

print(Solution())