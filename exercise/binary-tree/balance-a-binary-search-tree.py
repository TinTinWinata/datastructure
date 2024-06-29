from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.height = 1

class Solution(object):
    def get_height(self, root):
        if root is None:
          return 0
        if root.height is None:
          return 1
        return root.height
    
    def update_height(self, root):
        root.height = max(self.get_height(root.left), self.get_height(root.right)) + 1

    def left_rotate(self, root):
       parent = root.right

       left_parent = parent.left
       parent.left = root
       root.right = left_parent

       self.update_height(root)
       self.update_height(parent)

       return parent
    
    def right_rotate(self, root):
       parent = root.left
       right_parent = parent.right

       parent.right = root
       root.left = right_parent

       self.update_height(root)
       self.update_height(parent)

       return parent

    def get_bf(self, root):
       return self.get_height(root.left) - self.get_height(root.right)

    def check_rotate(self, root, val):
       bf = self.get_bf(root)
       if bf < -1 and val < root.right.val:
          root.right = self.right_rotate(root.right)
          return self.left_rotate(root)
       elif bf < -1: 
          return self.left_rotate(root)
       elif bf > 1 and val > root.left.val:
          root.left = self.left_rotate(root.left)
          return self.right_rotate(root)
       elif bf > 1:
          return self.right_rotate(root)
       return root

    def insert(self, root, val):
       if root is None:
          return TreeNode(val)
       if val < root.val:
          root.left = self.insert(root.left, val)
       elif val > root.val:
          root.right = self.insert(root.right, val)
       self.update_height(root)
       return self.check_rotate(root, val)

    def dfs(self, root):
       if root is None:
          return root

    def balanceBST(self, root):
        queue = deque([root])
        new_root = TreeNode(root.val)

        while queue:
           current = queue.popleft()
           if current.left:
              queue.append(current.left)
           if current.right:
              queue.append(current.right)
           new_root = self.insert(new_root, current.val)
        return new_root
           
        

# Example test case
if __name__ == "__main__":
    # Create an unbalanced BST
    root = TreeNode(1)
    root.right  = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    def print_result(root):
      if root is None:
          return
      print("Root : ", root.val)
      print_result(root.left)
      print_result(root.right)

    # Balance the BST
    solution = Solution()
    balanced_root = solution.balanceBST(root)
    print_result(balanced_root)

