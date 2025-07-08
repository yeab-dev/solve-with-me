from typing import List
from typing import Dict
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def validateAnagram(dict1: Dict[str,int], dict2: Dict[str,int]) -> bool:
            for key in dict1:
                if not key in dict2 or dict1[key] != dict2[key]:
                    return False
            for key in dict2:
                if not key in dict1 or dict1[key] != dict1[key]:
                    return False
            return True
        
        pt = dict(Counter(p))
        size = len(p)
        res = []
        for i in range(len(s)):
            st = dict(Counter(s[i:i + size]))
            if validateAnagram(st, pt):
                res.append(i)
        return res