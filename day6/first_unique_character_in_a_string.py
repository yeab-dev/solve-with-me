from collections import Counter
class Solution:
    def firstUniqueChar(self, s:str) -> int:
        count = dict(Counter(s))
        for key, value in count.items():
            if value == 1:
                return s.index(key)
        return -1