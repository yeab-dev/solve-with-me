from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, j = 0, len(s1)
        ref = Counter(s1)
        while j <= len(s2):
            sub = Counter(s2[i:j-i]) if i == 0 else Counter(s2[i:j])
            for char in ref:
                if ref[char] != sub[char]:
                    i += 1
                    j += 1
                    break
            else: return True
    
        return False