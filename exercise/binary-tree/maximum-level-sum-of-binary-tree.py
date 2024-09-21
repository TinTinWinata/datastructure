from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((1, root))
        result = dict()
        while queue:
            level, node = queue.popleft()

            if level in result:
                result[level] += node.val
            else:
                result[level] = node.val     

            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))

        max_value = float('-inf')
        max_level = None
        for level in result.keys():
            v = result[level]
            if v > max_value:
                max_value = v
                max_level = level
        return max_level