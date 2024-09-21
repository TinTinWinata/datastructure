from typing import Optional, List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def search(self, root: Optional[TreeNode], search: int):
        self.found = False
        self.founded_ancestors = []
        self.dfs(root, search, [])
        return self.founded_ancestors.copy()
    
    def dfs(self, root: Optional[TreeNode], search: int, ancestors: List[int]):
        if root is None or self.found:
            return
        ancestors.append(root)
        if search == root.val:
            self.found = True
            self.founded_ancestors = ancestors
            return
        self.dfs(root.left, search, ancestors.copy())
        self.dfs(root.right, search, ancestors.copy())
        

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors_p = self.search(root, p.val)
        ancestors_q = self.search(root, q.val)
        result = 0
        for i in range(min(len(ancestors_p), len(ancestors_q))):
            if ancestors_p[i].val != ancestors_q[i].val:
                break
            result = ancestors_q[i]
        return result