from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_diff = [0] * (n + 1)
        
        for start, end, direction in shifts:
            if direction == 1:
                prefix_diff[start] += 1
                if end + 1 < n + 1:
                    prefix_diff[end + 1] -= 1
            else:
                prefix_diff[start] -= 1
                if end + 1 < n + 1:
                    prefix_diff[end + 1] += 1
        
        res = []
        current_shift = 0
        for i in range(n):
            current_shift += prefix_diff[i]
            original_char = s[i]
            new_order = ord(original_char) - ord('a') + current_shift
            new_order %= 26
            new_char = chr(ord('a') + new_order)
            res.append(new_char)
        
        return ''.join(res)