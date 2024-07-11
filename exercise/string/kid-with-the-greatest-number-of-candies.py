from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandy = max(candies)
        res = []
        for v in candies:
            if v + extraCandies >= maxCandy:
                res.append(True)
            else:
                res.append(False)
        return res