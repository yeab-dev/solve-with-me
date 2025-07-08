from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i, j = 0,1
        sum = nums[i]
        res = 0
        if nums[i] > target:
            return 1
        while j < len(nums):
            sum += nums[j]
            if sum < target:
                j += 1
                continue
            res = min(res, j-i+1) if not res == 0 else j-i+1
            sum -= nums[i] + nums[j]
            i += 1
        return res