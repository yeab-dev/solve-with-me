from typing import List
import math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answerMap = {}
        res = 0
        for answer in answers:
            if answer == 0 or answer not in answerMap:
               answerMap[answer] = [1, answer+1]
               res += answer + 1
            else:
                answerMap[answer][0] += 1
                if answerMap[answer][0] > answerMap[answer][1]:
                    answerMap[answer][1] += answer + 1
                    res += answer + 1
        return res