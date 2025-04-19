from typing import List
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[1]-x[0])
        res = 0
        length = len(costs)
        for i in range(length):
            if i < length // 2:
                res += costs[i][1]
            else:
                res += costs[i][0]
        return res