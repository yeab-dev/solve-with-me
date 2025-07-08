from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        i,j = 0,1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums[i] += nums[j]
                nums[j] = 0
            i += 1
            j += 1
        i = 0
        num_of_zeros = nums.count(0)
        while i < len(nums) - num_of_zeros:
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i +=1
        return nums