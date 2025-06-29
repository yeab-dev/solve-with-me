from typing import List
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left: List[int], right: List[int]):
            result = []
            i,j = 0,0
            while i < len(left) and j < len(right):
                if left[i] >= right[j]:
                    result.append(right[j])
                    j += 1
                else:
                    result.append(left[i])
                    i += 1
            result.extend(left[i:])
            result.extend(right[j:])

            return result
        
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return merge(left, right)