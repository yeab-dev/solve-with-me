from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        def pascal(nums: List[int], index: int):
            nums.insert(0,0)
            nums.append(0)
            for i in range(len(nums)-1):
                nums[i] = nums[i] + nums[i+1]
            index += 1

            if index == rowIndex:
                return nums[:-1]
            return pascal(nums[:-1], index) 
        return pascal([1], 0)