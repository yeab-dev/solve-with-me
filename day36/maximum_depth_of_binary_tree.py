from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0

        def calDepth(node: Optional[TreeNode], d: int):
            if not node:
                return d
            return max(calDepth(node.left, d+1), calDepth(node.right, d+1))
        return calDepth(root, depth)