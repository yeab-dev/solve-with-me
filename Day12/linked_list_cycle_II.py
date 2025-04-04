from typing import Optional
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tor = head.next
        hare = head.next.next


        while tor is not hare:
            if not hare or not hare.next:
                return None
            tor = tor.next
            hare = hare.next.next
        return type(hare.next)

head = ListNode(3)
head.next = ListNode(2)
head.next.next = ListNode(0)
head.next.next.next = ListNode(-4)
head.next.next.next.next = head.next

print(Solution().detectCycle(head))