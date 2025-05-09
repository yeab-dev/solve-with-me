from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums)):
            if stack and nums[stack[-1]] < nums[i]:
                while stack and nums[stack[-1]] < nums[i]:
                    res[stack.pop()] = nums[i]
            stack.append(i)
        if stack:
            i = 0
            while i < len(nums):
                if nums[stack[-1]] < nums[i]:
                    res[stack.pop()] = nums[i]
                else:
                    i += 1
        return res