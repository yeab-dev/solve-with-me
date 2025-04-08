from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        res = [arr[0], arr[1]] if arr[0] != arr[1] else [arr[0]]
        maxLength = 0
        i = 1

        while i < len(arr)-1:
            sign = '<' if arr[i] > arr[i-1] else '>'
            if (arr[i+1] > arr[i] and sign == '>'):
                res.append(arr[i+1])
                i += 1
            elif (arr[i+1] < arr[i] and sign == '<'):
                res.append(arr[i+1])
                i += 1
            else:

                maxLength = max(len(res), maxLength)
                res = [arr[i], arr[i+1]] if arr[i] != arr[i+1] else [arr[i]]
                i += 1
        return max(maxLength, len(res))