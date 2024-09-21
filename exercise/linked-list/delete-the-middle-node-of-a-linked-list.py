from typing import Optional
from math import ceil

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        cursor = head

        while cursor:
            n += 1
            cursor = cursor.next

        if n == 1:
            return None
        
        cursor = head
        for _ in range(n // 2 - 1):
            cursor = cursor.next
        
        cursor.next = cursor.next.next

        return head