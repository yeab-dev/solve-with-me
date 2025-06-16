from typing import Optional
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root: return 

        def get_next(node: Optional[Node]):
            while node:
                if node.left:
                    return node.left
                if node.right:
                    return node.right
                node = node.next
            
            return
        
        if root.left:
            if root.right:
                root.left.next = root.right
            else:
                root.left.next = get_next(root.next)
        
        if root.right:
            root.right.next = get_next(root.next)
        
        self.connect(root.right)
        self.connect(root.left)

        return root