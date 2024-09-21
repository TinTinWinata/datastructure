from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], targetSum: int, possibilities: List[int]):
        if root is None:
            return
        new_possibilities = []
        for v in possibilities:
            new_sum  = v + root.val
            if new_sum  == targetSum:
                self.result += 1
            new_possibilities.append(new_sum)

        if root.val == targetSum:
            self.result += 1

        new_possibilities.append(root.val)
        self.dfs(root.left, targetSum, new_possibilities.copy())
        self.dfs(root.right, targetSum, new_possibilities.copy())

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.result = 0
        self.dfs(root, targetSum, [])
        return self.result