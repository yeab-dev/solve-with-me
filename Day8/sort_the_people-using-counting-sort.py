from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        max_height = max(heights)  # Find max height
        count = [[] for _ in range(max_height + 1)]  # Create counting array

        for name, height in zip(names, heights):
            count[height].append(name)

        sorted_names = []
        for h in range(max_height, -1, -1):
            if count[h]:
                sorted_names.extend(count[h])

        return sorted_names