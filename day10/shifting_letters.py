from typing import List
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        strList = list(s)
        for i in range(len(s)-2, -1, -1):
            shifts[i] += shifts[i+1]
        
        for i, shift in zip(range(len(s)), shifts):
            originalChar = strList[i]
            newOrder = ord(originalChar) - ord('a') + shift
            newOrder %= 26
            strList[i] = chr(newOrder + ord('a'))
        return "".join(strList)