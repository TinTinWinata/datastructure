class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class BinaryTree:
  def insert(self, root, val):
    if root is None:
      root = Node(val)
    elif val >= root.val:
      root.right = self.insert(root.right, val)
    elif val < root.val :
      root.left = self.insert(root.left, val)
    return root
  
  def preorder_print(self, root):
    if root is not None:
      self.preorder_print(root.left)
      self.preorder_print(root.right)

b = BinaryTree()
root = Node(5)

b.insert(root, 7)
b.insert(root, 9)

b.preorder_print(root)