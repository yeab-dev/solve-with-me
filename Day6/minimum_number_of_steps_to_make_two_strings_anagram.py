from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        s_count = dict(Counter(s))
        t_count = dict(Counter(t))
        result = 0
        for char, count in s_count.items():
            chars_in_t = t_count.get(char, 0)
            if chars_in_t < count:
                result += abs(count - chars_in_t)
        return result