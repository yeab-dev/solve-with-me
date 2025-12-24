from typing import List
class Solution:
    def minimumBoxes(self, apples:List[int], capacity: List[int])-> int:
        apples.sort()
        capacity.sort()
        totalApples = sum(apples)
        boxCount = 0
        while totalApples > 0:
            totalApples -= capacity.pop()
            boxCount+=1
        return boxCount