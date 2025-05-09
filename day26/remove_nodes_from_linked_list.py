from typing import Optional
class ListNode:
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNodes(self, head: Optional[ListNode]):
        stack = []

        while head:
            if stack and stack[-1] < head.val:
                while stack and stack[-1] < head.val:
                    stack.pop()
            stack.append(head.val)
            head = head.next
        
        dummy = ListNode(val=0)
        tmp = dummy
        for value in stack:
            tmp.next = ListNode(val=value)
            tmp = tmp.next

        return dummy.next