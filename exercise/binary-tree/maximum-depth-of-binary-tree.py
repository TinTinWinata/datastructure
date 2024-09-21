from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], height) -> int:
        if root is None:
            return height - 1
        return max(self.dfs(root.left, height+1), self.dfs(root.right, height+1))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)