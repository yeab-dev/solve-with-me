from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return
        
        root = TreeNode(preorder.pop(0))
        nextRootIdx = inorder.index(root.val)
        root.left = self.buildTree(preorder, inorder[:nextRootIdx])
        root.right = self.buildTree(preorder, inorder[nextRootIdx+1:])
        return root