from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums:List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        result = []
        keys = list(count.keys())
        values = list(count.values())
        while len(result) < k:
            maximum = max(values)
            index_of_max = values.index(maximum)
            result.append(keys[index_of_max])
            keys.pop(index_of_max)
            values.pop(index_of_max)
        return result