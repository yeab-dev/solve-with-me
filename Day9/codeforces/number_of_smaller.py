from typing import List
sizes = list(map(int, input().split()))

arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

def smaller(arr1: List[int], arr2: List[int]):
    i, count = 0, 0
    res = []
    for j in range(len(arr2)):
        while i < len(arr1) and arr2[j]> arr1[i]:
            count += 1
            i += 1
        res.append(count)
    for num in res:
        print(num, end=" ")

smaller(arr1, arr2)
    