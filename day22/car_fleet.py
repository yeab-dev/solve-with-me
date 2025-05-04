from typing import List
class Solution:
    def carFleet(self, target:int, position: List[int], speed: List[int]) -> int:
        stack = []
        posAndSpeed = [(i,j) for i,j in zip(position, speed)]
        posAndSpeed.sort(key=lambda x: x[0], reverse=True)

        for pos, sp in posAndSpeed:
            timeToReach = (target - pos) / sp
            if not stack or timeToReach > stack[-1]:
                stack.append(timeToReach)
        return len(stack)

#Initially my code wasn't this one. After solving it trying to optimize 
# the code with the help of an AI led me to this version of the solution. ;)