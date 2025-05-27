from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def calPathSum(node: Optional[TreeNode], sum: int) -> bool:
            if not node:
                return False
            if not (node.left or node.right):
                return sum + node.val == targetSum
            else:
                return calPathSum(node.left, sum+node.val) or calPathSum(node.right, sum+node.val)
        return calPathSum(root, 0)