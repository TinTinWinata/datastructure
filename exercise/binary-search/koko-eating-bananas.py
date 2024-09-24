from typing import List
from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        def validateIsCanK(k: int):
            nonlocal piles
            nonlocal h
            totalH = 0
            for v in piles:
                totalH += ceil(v / k)
                if totalH > h:
                    return False
            return True
        result = 0
        def binarySearch(left: int, right: int):
            nonlocal result
            if left > right:
                return
            mid = ((right - left) // 2) + left
            if validateIsCanK(mid):
                result = mid
                binarySearch(left, mid - 1)
            else:
                binarySearch(mid + 1, right)
        binarySearch(1, max_piles)
        return result
        
print(Solution().minEatingSpeed([30,11,23,4,20], 5))