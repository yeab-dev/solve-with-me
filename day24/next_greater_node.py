from typing import Optional
from typing import List
class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nodes = []
        stack = [] 

        while head:
            nodes.append(head.val)
            head = head.next

        res = [0] * len(nodes)

        for i in range(len(nodes)):
            if stack and nodes[stack[-1]] < nodes[i]:
                while stack and nodes[stack[-1]] < nodes[i]:
                    res[stack.pop()] = nodes[i]
            stack.append(i)
        return res