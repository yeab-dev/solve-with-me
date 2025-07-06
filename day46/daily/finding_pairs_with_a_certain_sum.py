from typing import List, Counter
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums1Count = Counter(nums1)
        self.nums2Count = Counter(nums2)
        pass

    def add(self, index: int, val: int) -> None:
        sum = self.nums2[index] + val
        removed = self.nums2[index]
        self.nums2[index] = sum

        if sum in self.nums2Count:
            self.nums2Count[sum] += 1
        else:
            self.nums2Count[sum] = 1
        
        if self.nums2Count[removed] > 1:
            self.nums2Count[removed] -= 1
        else:
            del self.nums2Count[removed]
    def count(self, tot: int) -> int:
        res = 0
        nums1Count = self.nums1Count
        nums2Count = self.nums2Count

        for num, freq in nums1Count.items():
            diff =  tot - num
            if diff in self.nums2Count:
                res += freq * nums2Count[diff]
        return res

fsp = FindSumPairs([1,1,2,2,2,3], [1,4,5,2,5,4])
print(fsp.count(7))
fsp.add(3,2)
print(fsp.count(8))
print(fsp.count(4))
fsp.add(0,1)
fsp.add(1,1)
print(fsp.count(7))