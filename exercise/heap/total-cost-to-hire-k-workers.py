import heapq
from collections import deque
from typing import List
class Node:
    def __init__(self, v, left):
        self.v = v
        self.left = left

    def __lt__(self, other):
        return self.v < other.v

class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        heap = []
        arr = deque(costs)
        n = len(costs)
        if n >= candidates * 2:
            for _ in range(candidates):
                heapq.heappush(heap, Node(arr.popleft(), True))
                heapq.heappush(heap, Node(arr.pop(), False))
        else:
            for v in costs:
                heapq.heappush(heap, Node(v, True))
            arr = []
        result = 0
        while k > 0:
            node = heapq.heappop(heap)
            result += node.v
            if arr:
                heapq.heappush(heap, Node(arr.popleft(), node.left) if node.left else Node(arr.pop(), node.left))
            k -= 1
        return result

print(Solution().totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58],11,2))
# print(Solution().totalCost([17,12,10,2,7,2,11,20,8], 3, 4))
# print(Solution().totalCost([1,2,4,1], 3, 3))