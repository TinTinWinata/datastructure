from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], leaves: List[int]):
        if root is None:
            return
        if root.left is None and root.right is None:
            leaves.append(root.val)
        self.dfs(root.left, leaves)
        self.dfs(root.right, leaves)
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1_leaves = []
        root2_leaves = []
        self.dfs(root1, root1_leaves)
        self.dfs(root2, root2_leaves)
        if len(root1_leaves) != len(root2_leaves):
            return False
        for i, v in enumerate(root1_leaves):
            if i >= len(root2_leaves) or v != root2_leaves[i]:
                return False
        return True