from typing import List
from collections import defaultdict
class Solution:
    def subarraySum(self,nums: List[int], k: int) -> int:
        prefixMap = defaultdict(int)
        res = 0
        sum = 0
        prefixMap[0] = 1
        for num in nums:
            sum += num
            if sum-k in prefixMap:
                res += prefixMap[sum-k]
            prefixMap[sum] += 1
        return res