from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def dfs(self, root: Optional[TreeNode], to_delete: List[int], forest: List[TreeNode]):
        if root is None or len(to_delete) == 0:
            return root
        # print(f'root {root.val} | forest len : {len(forest)}')
        if root.val in to_delete:
            # print('Seen to be deleted : ', root.val)
            # print('before delete')
            # for i, v in enumerate(forest):
            #    print(f'[{i}] v : ', v.val)
            for i, curr in enumerate(forest):
               if curr.val == root.val:
                  del forest[i]
                  break
            # print('after delete')
            # for i, v in enumerate(forest):
            #     print(f'[{i}] v : ', v.val)

            to_delete.remove(root.val)
            if root.left is not None:
              forest.append(root.left)
              root.left = self.dfs(root.left, to_delete, forest)

            if root.right is not None:
              forest.append(root.right)
              root.right = self.dfs(root.right, to_delete, forest)
            return None
        else:
          root.left = self.dfs(root.left, to_delete, forest)
          root.right = self.dfs(root.right, to_delete, forest)
          return root
            
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []
        forest =[root]
        self.dfs(root, to_delete, forest)
        return forest
    
# Test case 1: Deleting a single node
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)

to_delete = [2, 3]
result = Solution().delNodes(root, to_delete)

def printNode(node):
   if node is None: 
      return
   print(node.val)
   printNode(node.left)
   printNode(node.right)

for i, node in enumerate(result):
   print('iteration - ', i)
   printNode(node)