from typing import Optional
class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.result = None

        def inorder(node: TreeNode):
            if not node:
                return
            inorder(node.left)
            if root.val < node.val:
                if not self.result:
                    self.result = node.val
                elif self.result  > node.val:
                    self.result = node.val
            inorder(node.right)
        inorder(root)
        return self.result if not self.result else -1