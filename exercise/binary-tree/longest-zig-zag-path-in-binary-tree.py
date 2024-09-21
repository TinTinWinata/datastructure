from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], direction: str | None, zigZagCount: int):
        if root is None:
            return zigZagCount  
        return max(self.dfs(root.left, 'left', zigZagCount + 1 if direction == 'right' else 0)
        ,self.dfs(root.right, 'right', zigZagCount + 1 if direction == 'left' else 0))
    
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, None, 0)