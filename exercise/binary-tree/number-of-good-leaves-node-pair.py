from typing import List, Optional, Tuple

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchLeaves(self, root: Optional[TreeNode], leaves: List[Tuple[int, TreeNode]], distance = 0):
        if root is None:
            return
        if root.left is None and root.right is None:
            leaves.append((distance, root))
            return
        if root.left:
          self.searchLeaves(root.left, leaves, distance + 1)
        if root.right:
          self.searchLeaves(root.right, leaves, distance + 1)
    
    def dfs(self, root: Optional[TreeNode], distance: int):
        if root is None:
            return
        
        leftLeaves = []
        rightLeaves = []
        if root.left or root.right:
          if root.left:
              self.searchLeaves(root.left, leftLeaves)
          if root.right:
              self.searchLeaves(root.right, rightLeaves)
        
        # print(f'Root {root.val}')
        for (leftDistance, vLeft) in leftLeaves:
            for (rightDistance, vRight) in rightLeaves:
                 if leftDistance + rightDistance + 2 <= distance:
                    #  print(f'Founded {vLeft.val}[{leftDistance}] and {vRight.val}[{rightDistance}]')
                     self.result += 1
        
        self.dfs(root.left, distance)
        self.dfs(root.right, distance)

    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.result = 0
        self.dfs(root, distance)
        return self.result
    

# Test Cases 1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
print(Solution().countPairs(root, 3))


# Test Cases 2
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(7)
root.right.left = TreeNode(6)
print(Solution().countPairs(root, 3))