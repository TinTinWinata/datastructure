# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        cursor = head;
        criticals = []
        i = 0
        while cursor.next.next is not None:
            if (cursor.next.val < cursor.val and cursor.next.val < cursor.next.next.val) or (cursor.next.val > cursor.val and cursor.next.val > cursor.next.next.val):
                criticals.append(i)
            
            i += 1
            cursor = cursor.next
        
        n = len(criticals)

        if n < 2:
            return [-1, -1]
        
        min_distance = float('inf')
        for i in range(n - 1):
            min_distance = min(min_distance, criticals[i + 1] - criticals[i])
        
        return [min_distance, criticals[-1] - criticals[0]]
            
        