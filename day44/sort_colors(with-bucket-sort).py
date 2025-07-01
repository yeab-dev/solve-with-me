from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        res = [0] * 3
        for num in nums:
            res[num] += 1
        nums.clear()
        for i in range(len(res)):
            while res[i] > 0:
                nums.append(i)
                res[i] -= 1