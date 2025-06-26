class Solution:
    def climbingStairs(self, n: int) -> int:
        stairCach = {}
        def countStairs(n):
            if n == 0 or n == 1:
                return 1
            if n not in stairCach:
                stairCach[n] = countStairs(n-1) + countStairs(n-2)
            return stairCach[n]
        return countStairs(n)

print(Solution().climbingStairs(5))