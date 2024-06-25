# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def dfs(self, root, carry = 0):
          if not root:
              return 0

          res = self.dfs(root.right, carry)

          res += root.val + (carry if not root.right else 0) 
          left_res = self.dfs(root.left, res)   
          # print(f'root val {root.val} | res {res} | carry {carry}')
          root.val = res
          return max(left_res, res)
    
    def bstToGst(self, root):
        self.dfs(root)
        return root

# Test case
root = TreeNode(4)
root.left = TreeNode(1)
root.right = TreeNode(6)
root.left.left = TreeNode(0)
root.left.right = TreeNode(2)
root.left.right.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)

# root = TreeNode(3)
# root.left = TreeNode(2)
# root.right = TreeNode(4)
# root.left.left = TreeNode(1)

solution = Solution()
gst_root = solution.bstToGst(root)
