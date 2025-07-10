from typing import List
class Solution:
    def subsets(self, nums: List[int])-> List[List[int]]:
        res = []

        subsets = []
        def dfs(i: int):
            if i >= len(nums):
                res.append(subsets.copy())
                return
            subsets.append(nums[i])
            dfs(i+1)

            subsets.pop()
            dfs(i+1)
        dfs(0)
        return res

print(Solution().subsets([1,2,3]))
