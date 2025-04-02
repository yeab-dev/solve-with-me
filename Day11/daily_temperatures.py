from typing import List
from collections import defaultdict
class Solution:
    def dailyTemperatures(self, temperatures:List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd

            stack.append([t, i])
        return res 