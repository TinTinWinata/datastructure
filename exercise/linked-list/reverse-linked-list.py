from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left_p = None
        cursor = head
        while cursor:
            temp = cursor
            cursor = cursor.next

            temp.next = left_p
            left_p = temp

        return left_p