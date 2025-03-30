from collections import Counter
from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_freq = Counter(arr1)
        res = []
        nums = []
        for num in arr2:
            for _ in range(arr1_freq[num]):
                res.append(num)
        
        for num in arr1_freq:
            if not num in arr2:
                for _ in range(arr1_freq[num]):
                    nums.append(num)
        res.extend(sorted(nums))
        return res