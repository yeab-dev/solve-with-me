from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        
        root = TreeNode(postorder.pop())

        nextRootIdx = inorder.index(root.val)
        root.right = self.buildTree(inorder[nextRootIdx+1:], postorder)
        root.left = self.buildTree(inorder[:nextRootIdx], postorder)
        return root