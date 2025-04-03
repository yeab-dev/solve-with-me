from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        cur = head
        while cur.next:
            cur = cur.next
            count += 1

        for _ in range(count // 2):
            head = head.next            
        return head