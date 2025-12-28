from typing import List
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        prefixSum = [0] * len(arr)
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
            prefixSum[i] = sum
        length = 1
        result = 0
        while length <= len(arr):
            for i in range(len(arr) - 1, -1, -1):
                if (i - length == -1):
                    result += prefixSum[i]
                    break
                else: result += prefixSum[i] - prefixSum[i-length]
            length += 2
        return result