from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
class Solutions:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(left: Optional[ListNode], right: Optional[ListNode]):
            mergedList = ListNode(0)
            current = mergedList
            while left and right:
                if left.val < right.val:
                    current.next = left
                    left = left.next
                else:
                    current.next = right
                    right = right.next
                
                current = current.next
            if left:
                current.next = left
            if right:
                current.next = right
            return mergedList.next
        
        if len(lists) <= 1:
            return lists[0] if lists else None
        
        mid = len(lists) // 2
        left = self.mergeKLists(lists=lists[:mid])
        right = self.mergeKLists(lists=lists[mid:])

        return merge(left=left, right=right)