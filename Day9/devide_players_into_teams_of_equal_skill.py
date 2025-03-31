from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        i,j = 0, len(skill)-1
        teams = 0
        chemistry = 0
        target = skill[i] + skill[j]
        while i < j:
            if skill[i] + skill[j] == target:
                teams += 1
                chemistry += skill[i] * skill[j]
            i += 1
            j -= 1
        if (chemistry == skill[0] * skill[len(skill)-1] and not len(skill) == 2) or teams != len(skill) // 2:
            return -1
        return chemistry 
