class Solution:
    def balanceBST(self, root):
        def in_order_traversal(node):
            if not node:
                return []

            return in_order_traversal(node.left) + [node.val] + in_order_traversal(node.right)

        def build_balanced_bst(elements):
            if not elements:
                return None
            mid = len(elements) // 2
            node = TreeNode(elements[mid])
            node.left = build_balanced_bst(elements[:mid])
            node.right = build_balanced_bst(elements[mid + 1:])
            return node

        sorted_elements = in_order_traversal(root)
        print('Sorted Elements : ', sorted_elements)
        return build_balanced_bst(sorted_elements)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

if __name__ == "__main__":
    # Create an unbalanced BST
    root = TreeNode(1)
    root.right  = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)

    def print_result(root):
      if root is None:
          return
      print(f"Left [{root.val}]")
      print_result(root.left)
      print(f"Right [{root.val}]")
      print_result(root.right)

    # Balance the BST
    solution = Solution()
    balanced_root = solution.balanceBST(root)
    print_result(balanced_root)
