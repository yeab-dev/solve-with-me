from typing import List
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        minOps = 0
        for log in logs:
            if log == "../":
                if minOps >= 1:
                    minOps -= 1
            elif log != "./":
                minOps += 1
        return minOps