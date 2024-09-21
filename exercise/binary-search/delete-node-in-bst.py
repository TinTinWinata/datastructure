from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left and root.right is None:
                return root.left
            elif root.right and root.left is None:
                return root.right
            elif root.right is None and root.left is None:
                return None
            
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            
            root.val, successor.val = successor.val, root.val
            root.right = self.deleteNode(root.right, successor.val)

        return root
        