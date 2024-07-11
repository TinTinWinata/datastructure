def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "\n")
        current = current.next

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeNodes(self, head):
        new_head = None
        tail = None
        right_p = head.next
        while True:
            val_sum = 0
            while right_p.val != 0:
                val_sum += right_p.val
                right_p = right_p.next
            
            new_node = ListNode(val_sum)
            
            if tail is not None:
                tail.next = new_node
            else:
                new_head = new_node
            tail = new_node

            if right_p.next == None:
                break
            else:
                right_p = right_p.next
                continue
        return new_head
            

# Creating the linked list for the test case: 0 -> 3 -> 1 -> 0 -> 4 -> 5 -> 2 -> 0
node7 = ListNode(0)
node6 = ListNode(2, node7)
node5 = ListNode(5, node6)
node4 = ListNode(4, node5)
node3 = ListNode(0, node4)
node2 = ListNode(1, node3)
node1 = ListNode(3, node2)
head = ListNode(0, node1)

# print("Before merged:")
# print_linked_list(head)

# Applying the mergeNodes method
sol = Solution()
merged_head = sol.mergeNodes(head)

# Printing the result
print("Merged linked list:")
print_linked_list(merged_head)
