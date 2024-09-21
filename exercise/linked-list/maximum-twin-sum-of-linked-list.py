from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution: 
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # 1. Get Middle
        cursor = head
        n = 1
        while cursor:
            n += 1
            cursor = cursor.next

        cursor = head
        for _ in range(n // 2 - 1):
            cursor = cursor.next

        mid = cursor

        # 2. Reverse From middle to right
        cursor = cursor.next
        left_p = None
        
        while cursor:
            temp = cursor
            cursor = cursor.next
            temp.next = left_p
            left_p = temp
        
        mid.next = left_p
        mid = mid.next

        # Make 2 pointer from (first -> middle) (middle -> end)
        result = 0
        cursor = head
        for _ in range(n // 2):
            result = max(result, cursor.val + mid.val)
            cursor = cursor.next
            mid = mid.next
        return result
