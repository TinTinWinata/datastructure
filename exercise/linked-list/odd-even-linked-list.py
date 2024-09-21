from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        cursor = head
        odd_head = None
        even_head = None
        odd_tail = None
        even_tail = None

        idx = 1
        while cursor:
            if idx % 2 == 0:
                if even_head is None:
                    even_head = cursor
                    even_tail = cursor
                else:
                    even_tail.next = cursor
                    even_tail = cursor
            else:
                if odd_head is None:
                    odd_head = cursor
                    odd_tail = cursor
                else:
                    odd_tail.next = cursor
                    odd_tail = cursor

            
            cursor = cursor.next
            idx += 1

        odd_tail.next = even_head

        if(even_tail is not None):
          even_tail.next = None

        return odd_head
    

# Helper function to convert a list into a linked list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Helper function to convert a linked list back to a Python list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        print('Current ', current.val)
        result.append(current.val)
        current = current.next
    return result

# Test case
input_list = [1]
head = create_linked_list(input_list)

# Create a solution instance
solution = Solution()

# Get the result
result_head = solution.oddEvenList(head)

# Convert the result linked list back to a Python list
output_list = linked_list_to_list(result_head)

# Print the output
print(output_list)