from typing import List
class Solution:
    def subarraysDivByK(self,nums: List[int], k: int) -> int:
        prefixMap = {}
        res = 0
        sum = 0
        prefixMap[0] = 1
        for num in nums:
            sum += num
            rem = sum % k
            if rem in prefixMap:
                res += prefixMap[rem]
                prefixMap[rem] += 1
            else:
                prefixMap[rem] = 1

        return res