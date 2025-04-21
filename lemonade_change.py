from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0]  != 5:
            return False
        
        fives = 1
        tens = 0

        for i in range(1, len(bills)):
            if bills[i] == 5:
                fives += 1
            elif bills[i] == 10:
                if fives < 1:
                    return False
                tens += 1
                fives -= 1
            else:
                if tens > 0 and fives > 0:
                    fives -= 1
                    tens -= 1
                elif fives > 2:
                    fives -= 3
                else:
                    return False
        return True