# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def dfs(self, root, max_value):
        if root is None:
            return
        if root.val >= max_value:
            self.count += 1
        self.dfs(root.left, max(max_value, root.val))
        self.dfs(root.right, max(max_value, root.val))
        
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root, root.val)
        return self.count