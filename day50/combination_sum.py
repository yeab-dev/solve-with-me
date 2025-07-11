from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        cand = []
        def dfs(index: int, total: int):
            if index >= len(candidates) or total >= target:
                if total == target:
                    result.append(cand.copy())
                return
            
            cand.append(candidates[index])
            total += candidates[index]
            dfs(index, total)

            cand.pop()
            total -= candidates[index]
            dfs(index+1, total)
        
        dfs(0, 0)
        return result