from typing import List
class Solution:    
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res =[]
        def flip(arr, k: int) -> None:
            res.append(k+1)
            left = 0
            while left < k:
                arr[left], arr[k] = arr[k], arr[left]
                k -= 1
                left += 1
        def max_index(arr, k: int) -> int:
            index = 0
            for i in range(k):
                if arr[i] > arr[index]:
                    index = i
            return index

        n = len(arr)
        while n > 1:
            maxidx = max_index(arr, n)
            if maxidx != n - 1:
                if maxidx != 0:
                    flip(arr, maxidx)
                flip(arr, n - 1)
            n -= 1
        return res

print(Solution().pancakeSort([3,2,4,1]))
