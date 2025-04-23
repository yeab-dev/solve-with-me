from typing import List
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        sizeMap = {}
        for i, size in enumerate(groupSizes):
            if size in sizeMap:
                if len(sizeMap[size])>= size:
                    res.append(sizeMap[size])
                    sizeMap[size] = [i]
                else:
                    sizeMap[size].append(i)
            else:
                sizeMap[size] = [i]
        
        for size in sizeMap:
            if sizeMap[size]:
                res.append(sizeMap[size])
        return res
