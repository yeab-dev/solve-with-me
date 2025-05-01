from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        if goal == 0:
            return True
        for i in range(goal-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0