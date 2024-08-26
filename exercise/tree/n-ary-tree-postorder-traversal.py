from typing import List, Optional

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def dfs(self, root: Optional[Node], numbers: List[int]):
        if(root is None):
            return
        for child in root.children:
            self.dfs(child, numbers)
        numbers.append(child.val)
        return
    def postorder(self, root: Node) -> List[int]:
        numbers = []
        self.dfs(root, numbers)
        return numbers
    