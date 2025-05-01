from typing import List
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        isSorted = False
        count = 0

        if nums == sorted(nums) or len(nums) == 1:
            return 0
        while not isSorted:
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    temp = nums[i]
                    nums[i] = temp - nums[i+1]
                    nums.insert(i+1, nums[i+1])
                    count += 1
            if nums == sorted(nums):
                isSorted = True
        return count

print(Solution().minimumReplacement([12,9,7,6,17,19,21]))