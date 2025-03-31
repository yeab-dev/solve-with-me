from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i, j = 0, 1
        while j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i += 1
            j = max(j, i + 1)
            while j < len(nums) and nums[j] == 0:
                j += 1
            if j < len(nums) and i < len(nums):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1  
                j += 1
