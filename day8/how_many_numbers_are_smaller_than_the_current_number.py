from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse=True)
        i = 0
        length = len(sorted_nums)
        count = {}
        while i < length -1:
            while i < length -1 and sorted_nums[i + 1] == sorted_nums[i]:
                i += 1
            count[sorted_nums[i]] = length - i - 1
            i += 1
        count[sorted_nums[length-1]] = 0

        res = [] 
        for num in nums:
            res.append(count[num])
        return res