from typing import List
from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr).items()
        lucky = -1
        for num, freq in count:
            if num == freq and num > lucky:
                lucky = num 
        return lucky

print(Solution().findLucky([1,2,2,3,3,3]))