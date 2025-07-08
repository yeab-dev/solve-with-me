class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        circle: list[int] = [num for num in range(1, n + 1, 1)]
        index: int = 0

        while len(circle) != 1:
            next_to_remove: int = (index + k - 1) % len(circle)
            circle.pop(next_to_remove)
            index = next_to_remove

        return circle[0]