from typing import List
from heapq import  heappop, heappush, heapify
from math import sqrt, ceil

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [v * -1 for v in gifts]
        heapify(gifts)
        for i in range(k):
            val = heappop(gifts)
            sqrt_val = ceil(sqrt(val * - 1) * -1)
            heappush(gifts, sqrt_val)
        return sum([v * -1 for v in gifts])

print(Solution().pickGifts([25,64,9,4,100], 4))