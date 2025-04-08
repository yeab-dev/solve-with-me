class Solution:
    def equalSubstring(self, s: str, t: str, maxCost) -> int:
        length = 0
        maxLength = 0
        cost = 0 
        i,j = 0,0

        while i < len(s) and j < len(s):
            if maxCost >= cost + abs(ord(s[j]) - ord(t[j])):
                cost += abs(ord(s[j]) - ord(t[j]))
                length += 1
                j += 1
                continue
            i += 1
            maxLength = max(length, maxLength)
            length, cost = length - 1, cost - abs(ord(s[i-1]) - ord(t[i-1]))
        return maxLength
