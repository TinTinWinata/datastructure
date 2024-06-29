class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None
    self.height = 1

class AVLTree:
  def insert(self, root, val):

    if root is None:
      root = Node(val)
    elif val >= root.val:
      root.right = self.insert(root.right, val)
    elif val < root.val :
      root.left = self.insert(root.left, val)
    self.update_height(root)
    return self.check_rotation(root, val)
  
  def get_balance_factor(self, root):
    return self.get_height(root.left) - self.get_height(root.right)

  def check_rotation(self, root, val):
    bf = self.get_balance_factor(root)
    # print(f'[{root.val}] balance factor : ', bf , f' height left {self.get_height(root.left)} | height right {self.get_height(root.right)}')
    if bf > 1 and val < root.left.val:
      return self.right_rotate(root)
    elif bf > 1 and val > root.left.val:
      root.left = self.left_rotate(root.left)
      return self.right_rotate(root)
    elif bf < -1 and val < root.right.val:
      root.right = self.right_rotate(root.right)
      return self.left_rotate(root)
    elif bf < -1 and val > root.right.val:
      return self.left_rotate(root)
    return root

  def get_height(self, root):
    if root is None:
      return 0
    return root.height

  def update_height(self, root):
    root.height = max(self.get_height(root.left) , self.get_height(root.right)) + 1

  def left_rotate(self, root):
    print('[left rotate] root : ', root.val)
    parent = root.right
    left_parent = parent.left

    parent.left = root
    root.right = left_parent

    self.update_height(root)
    self.update_height(parent)
    return parent
  
  def right_rotate(self, root):
    print('[right rotate] root : ', root.val)
    parent = root.left
    right_parent = parent.right

    parent.right = root
    root.left = right_parent

    self.update_height(root)
    self.update_height(parent)
    return parent

  def preorder_print(self, root):
    if root is not None:
      print('val : ', root.val)
      self.preorder_print(root.left)
      self.preorder_print(root.right)

b = AVLTree()
root = Node(5)
root = b.insert(root, 7)
root = b.insert(root, 6)
b.insert(root, 9)
b.insert(root, 10)
b.preorder_print(root)