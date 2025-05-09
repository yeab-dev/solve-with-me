from typing import List
class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack or (stack and num >= stack[-1]):
                stack.append(num)
        
        return len(stack)